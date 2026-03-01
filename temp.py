"""
Allure Aggregation Tool
-----------------------

Purpose:
This script accepts one or more GitLab pipeline IDs (parent or regular),
downloads their test job artifacts, extracts `target/allure-results`,
merges all results into a local `target/allure-results` directory,
and generates a single self-contained Allure HTML report.

Behavior:
- If pipeline ID has child pipelines → process children.
- If no child pipelines → treat as regular pipeline.
- Clears previous allure-results on every run.
- Skips corrupt/invalid zip entries safely.
- Generates single HTML report using Allure CLI jar
  located in same directory as this script.
- Output file includes timestamp for uniqueness.

Environment Variables Required:
  GITLAB_URL
  PROJECT_ID
  AGGREGATE_PIPELINE_IDS (comma separated)
  GITLAB_TOKEN

Optional:
  TEST_JOB_NAME (default: test)
  MAX_WORKERS (default: 4)

Output:
  target/consolidated-report-<timestamp>.html
"""

import os
import sys
import json
import time
import shutil
import zipfile
import tempfile
import subprocess
from datetime import datetime
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# -----------------------------
# CONFIGURATION
# -----------------------------

BASE_DIR       = Path(__file__).parent.resolve()
TARGET_DIR     = BASE_DIR / "target"
RESULTS_DIR    = TARGET_DIR / "allure-results"
REPORTS_DIR    = TARGET_DIR
ALLURE_JAR     = next(BASE_DIR.glob("allure-commandline*.jar"), None)

GITLAB_URL     = os.getenv("GITLAB_URL", "").rstrip("/")
PROJECT_ID     = os.getenv("PROJECT_ID")
PIPELINE_IDS   = os.getenv("AGGREGATE_PIPELINE_IDS")
TOKEN          = os.getenv("GITLAB_TOKEN")
TEST_JOB_NAME  = os.getenv("TEST_JOB_NAME", "test").lower()
MAX_WORKERS    = int(os.getenv("MAX_WORKERS", "4"))

if not all([GITLAB_URL, PROJECT_ID, PIPELINE_IDS, TOKEN]):
    print("Missing required environment variables.")
    sys.exit(1)

if not ALLURE_JAR or not ALLURE_JAR.is_file():
    print("Allure CLI jar not found in script directory.")
    sys.exit(1)

WRITE_LOCK = Lock()

# -----------------------------
# LOGGING
# -----------------------------

def log(level, message, **kwargs):
    print(json.dumps({"level": level, "message": message, **kwargs}))

# -----------------------------
# HTTP SESSION
# -----------------------------

def build_session():
    session = requests.Session()
    retry = Retry(
        total=4,
        backoff_factor=1.5,
        status_forcelist={429, 500, 502, 503, 504},
        allowed_methods={"GET"},
    )
    session.mount("https://", HTTPAdapter(max_retries=retry))
    session.mount("http://", HTTPAdapter(max_retries=retry))
    session.headers["PRIVATE-TOKEN"] = TOKEN
    session.verify = os.getenv("REQUESTS_CA_BUNDLE") or True
    return session

SESSION = build_session()

# -----------------------------
# GITLAB API
# -----------------------------

def validate_pipeline_ids(ids_str):
    ids = [x.strip() for x in ids_str.split(",")]
    for pid in ids:
        if not pid.isdigit():
            raise ValueError(f"Invalid pipeline ID: {pid}")
    return ids


def api_get_paginated(path):
    results, page = [], 1
    while True:
        resp = SESSION.get(
            f"{GITLAB_URL}/api/v4/{path}",
            params={"per_page": 100, "page": page},
            timeout=30,
        )
        resp.raise_for_status()
        data = resp.json()
        if not data:
            break
        results.extend(data)
        if len(data) < 100:
            break
        page += 1
    return results


def get_child_pipelines(pid):
    bridges = api_get_paginated(
        f"projects/{PROJECT_ID}/pipelines/{pid}/bridges"
    )
    return [
        str(b["downstream_pipeline"]["id"])
        for b in bridges
        if b.get("downstream_pipeline", {}).get("id")
    ]


def get_test_job_id(pid):
    jobs = api_get_paginated(
        f"projects/{PROJECT_ID}/pipelines/{pid}/jobs"
    )
    for job in jobs:
        if job["name"].lower() == TEST_JOB_NAME and job["status"] == "success":
            return job["id"]
    return None


# -----------------------------
# EXTRACTION
# -----------------------------

def download_and_extract(pid):
    start = time.perf_counter()

    job_id = get_test_job_id(pid)
    if not job_id:
        log("WARN", "No test job found", pipeline=pid)
        return 0, 0.0

    url = f"{GITLAB_URL}/api/v4/projects/{PROJECT_ID}/jobs/{job_id}/artifacts"
    extracted = 0
    dest = RESULTS_DIR.resolve()

    with SESSION.get(url, stream=True, timeout=60) as resp:
        resp.raise_for_status()
        tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".zip")
        try:
            for chunk in resp.iter_content(chunk_size=8192):
                tmp.write(chunk)
            tmp.close()

            with zipfile.ZipFile(tmp.name) as zf:
                for member in zf.infolist():
                    try:
                        name = member.filename.replace("\\", "/")
                        if "target/allure-results/" not in name or member.is_dir():
                            continue

                        # Zip-slip guard
                        target = (dest / f"{pid}_{Path(name).name}").resolve()
                        if dest not in target.parents:
                            log("WARN", "Zip-slip attempt blocked",
                                pipeline=pid, entry=member.filename)
                            continue

                        with WRITE_LOCK:
                            with zf.open(member) as src, open(target, "wb") as out:
                                shutil.copyfileobj(src, out)
                        extracted += 1

                    except Exception as e:
                        log("WARN", "Skipping invalid zip entry",
                            pipeline=pid, entry=member.filename, error=str(e))

        finally:
            os.unlink(tmp.name)

    return extracted, time.perf_counter() - start


# -----------------------------
# MAIN
# -----------------------------

def main():
    start_total = time.perf_counter()
    pipeline_ids = validate_pipeline_ids(PIPELINE_IDS)

    if RESULTS_DIR.exists():
        shutil.rmtree(RESULTS_DIR)
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    # Determine pipelines to process (auto-detect parent vs regular)
    pipelines = []
    for pid in pipeline_ids:
        children = get_child_pipelines(pid)
        pipelines.extend(children if children else [pid])

    pipelines = sorted(set(pipelines))
    if not pipelines:
        log("ERROR", "No pipelines to process")
        sys.exit(1)

    total_files = 0

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {executor.submit(download_and_extract, pid): pid for pid in pipelines}
        for future in as_completed(futures):
            pid = futures[future]
            try:
                files, duration = future.result()
                total_files += files
                log("INFO", "Processed pipeline",
                    pipeline=pid,
                    files=files,
                    duration_seconds=round(duration, 2))
            except Exception as e:
                log("ERROR", "Pipeline processing failed",
                    pipeline=pid, error=str(e))

    if total_files == 0:
        log("ERROR", "No Allure results extracted")
        sys.exit(1)

    # Generate single-file report
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_file = REPORTS_DIR / f"consolidated-report-{timestamp}.html"
    tmp_report  = REPORTS_DIR / "tmp-report"

    subprocess.run([
        "java", "-jar", str(ALLURE_JAR),
        "generate", str(RESULTS_DIR),
        "-o", str(tmp_report),
        "--clean",
        "--single-file",
    ], check=True, timeout=300)

    shutil.move(str(tmp_report / "index.html"), report_file)
    shutil.rmtree(tmp_report, ignore_errors=True)

    log("INFO", "Report generated",
        file=str(report_file),
        total_execution_seconds=round(time.perf_counter() - start_total, 2))


if __name__ == "__main__":
    main()
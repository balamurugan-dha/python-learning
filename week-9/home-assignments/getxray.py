import requests

BASE_URL = "https://your-jira.atlassian.net"
AUTH = ("email@example.com", "your_api_token")
HEADERS = {"Accept": "application/json"}

def get_all_tests():
    issues = []
    start = 0
    max_results = 100

    while True:
        response = requests.get(
            f"{BASE_URL}/rest/api/3/search",
            params={
                "jql": "issueType = Test",
                "fields": "customfield_11700,summary",
                "startAt": start,
                "maxResults": max_results
            },
            auth=AUTH,
            headers=HEADERS
        )
        data = response.json()
        issues.extend(data["issues"])

        if start + max_results >= data["total"]:
            break
        start += max_results

    return issues

def filter_less_than_two_plans(issues):
    results = []
    for issue in issues:
        plans = issue["fields"].get("customfield_11700") or []
        if len(plans) < 2:
            results.append({
                "key": issue["key"],
                "summary": issue["fields"].get("summary"),
                "test_plan_count": len(plans)
            })
    return results

tests = get_all_tests()
flagged = filter_less_than_two_plans(tests)

for t in flagged:
    print(f"{t['key']} | Plans: {t['test_plan_count']} | {t['summary']}")
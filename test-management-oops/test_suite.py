import csv


class TestSuite:

    def __init__(self, suite_name):
        self.suite_name = suite_name
        self.tests = []

    def add_test(self, test_case):
        self.tests.append(test_case)

    def run_all_tests(self):
        print(f"\nRunning Test Suite: {self.suite_name}")

        for test in self.tests:
            result = input(
                f"Enter result for {test.test_name} (Pass/Fail, Enter to skip): "
            ).strip().lower()

            if result == "":
                # User skipped → keep "Not Executed"
                continue
            elif result == "pass":
                test.execute_test("Pass")
            elif result == "fail":
                test.execute_test("Fail")
            else:
                print("Invalid input. Marked as Not Executed.")

    def save_results_to_csv(self, file_name):
        with open(file_name, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(
                ["Test ID", "Test Name", "Module", "Status", "Automation Tool"]
            )
            for test in self.tests:
                writer.writerow(test.to_csv_row())

    def summary_report(self):
        total = len(self.tests)
        passed = sum(1 for t in self.tests if t.status == "Pass")
        failed = sum(1 for t in self.tests if t.status == "Fail")
        not_executed = sum(1 for t in self.tests if t.status == "Not Executed")

        print("\nExecution Summary")
        print("-" * 30)
        print(f"{'Metric':<20} {'Count':<10}")
        print("-" * 30)
        print(f"{'Total Tests':<20} {total:<10}")
        print(f"{'Passed':<20} {passed:<10}")
        print(f"{'Failed':<20} {failed:<10}")
        print(f"{'Not Executed':<20} {not_executed:<10}")
        print("-" * 30)

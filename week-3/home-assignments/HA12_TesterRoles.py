import numpy as np

class ManualTester:
    def analyze(self, data):
        print(f"Manual Tester Analysis - First 5 execution times: {data[:5]}")

class AutomationTester:
    def analyze(self, data):
        print(f"Automation Tester Analysis - Fastest test case: {np.min(data)} seconds")

class PerformanceTester:
    def analyze(self, data):
        percentile_95 = np.percentile(data, 95)
        print(f"Performance Tester Analysis - 95th percentile: {percentile_95} seconds")

def show_analysis(tester, data):
    tester.analyze(data)

if __name__ == "__main__":
    execution_times = np.array([8.3, 12.5, 6.2, 15.7, 9.8, 22.1, 7.9, 18.4, 11.3, 14.6, 5.1, 20.8])
    
    print("Test Execution Analysis by Different QA Roles")
    print(f"All Execution Times: {execution_times}")
    print(f"Total Tests: {len(execution_times)}")
    print()
    
    manual_tester = ManualTester()
    automation_tester = AutomationTester()
    performance_tester = PerformanceTester()
    
    # demo polymorphism
    show_analysis(manual_tester, execution_times)
    show_analysis(automation_tester, execution_times)
    show_analysis(performance_tester, execution_times)
import numpy as np

class TestReport:
    def __init__(self, execution_times):
        self.execution_times = np.array(execution_times)
    
    def average_time(self):
        return np.mean(self.execution_times)
    
    def max_time(self):
        return np.max(self.execution_times)

class RegressionReport(TestReport):
    def __init__(self, execution_times):
        super().__init__(execution_times)
    
    def slow_tests(self, threshold):
        return self.execution_times[self.execution_times > threshold]

if __name__ == "__main__":
    execution_times = np.array([12.5, 8.3, 15.7, 6.2, 22.1, 9.8, 18.4, 7.9, 14.6, 11.3])
    
    regression_report = RegressionReport(execution_times)
    
    print("Test Execution Analysis")
    print(f"Execution Times: {regression_report.execution_times}")
    print(f"Average Time: {regression_report.average_time():.2f} seconds")
    print(f"Maximum Time: {regression_report.max_time():.2f} seconds")
    
    threshold = 15
    slow_tests = regression_report.slow_tests(threshold)
    print(f"Slow Tests (>{threshold} seconds): {slow_tests}")
    print(f"Number of Slow Tests: {len(slow_tests)}")
from test_case import TestCase
from automated_test_case import AutomatedTestCase
from test_suite import TestSuite


if __name__ == "__main__":
    # Create manual test cases
    tc1 = TestCase("TC001", "Login Test", "Authentication")
    tc2 = TestCase("TC002", "Logout Test", "Authentication")

    # Create automated test cases
    atc1 = AutomatedTestCase("TC003", "Add to Cart", "Shopping", "Selenium")
    atc2 = AutomatedTestCase("TC004", "Payment Flow", "Checkout", "Playwright")

    # Create test suite
    suite = TestSuite("Regression Suite")

    # Add tests to suite
    suite.add_test(tc1)
    suite.add_test(tc2)
    suite.add_test(atc1)
    suite.add_test(atc2)

    # Execute tests
    suite.run_all_tests()

    # Save results
    suite.save_results_to_csv("test_results.csv")

    # Show summary
    suite.summary_report()

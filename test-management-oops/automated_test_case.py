from test_case import TestCase


class AutomatedTestCase(TestCase):

    def __init__(self, test_id, test_name, module, automation_tool):
        super().__init__(test_id, test_name, module)
        self.automation_tool = automation_tool

    def display_test_case(self):
        print(self.test_id, self.test_name, self.module, self.status, self.automation_tool)

    def to_csv_row(self):
        return [self.test_id, self.test_name, self.module, self.status, self.automation_tool]
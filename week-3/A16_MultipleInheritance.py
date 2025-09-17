class Employee:
    def __init__(self, name):
        self.name = name

class AutomationSkills:
    def write_script(self):
        print(f"{self.name} is writing Selenium scripts")

class AutomationTester(Employee, AutomationSkills):
    def execute_tests(self):
        print(f"{self.name} is executing automation tests")

a1 = AutomationTester("Bala")
a1.write_script()
a1.execute_tests()

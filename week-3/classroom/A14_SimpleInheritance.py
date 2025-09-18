class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

class Tester(Employee):
    def __init__(self, name, employee_id):
        super().__init__(name, employee_id)

    def run_tests(self):
        print(f"Tester Name: {self.name} with Employee ID: {self.employee_id} is running automation tests.")

t1 = Tester("Bala", 23)
t1.run_tests()

t2 = Tester("Murugan", 41)
t2.run_tests()
class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, employee_id):
        super().__init__(name)
        self.employee_id = employee_id

class Manager(Employee):
    def __init__(self, name, employee_id, team_size):
        super().__init__(name, employee_id)
        self.team_size = team_size

    def show_details(self):
        print(f"Manager Name: {self.name}, Employee ID: {self.employee_id}, Team Size: {self.team_size}")

m1 = Manager("Bala", 23, 10)
m1.show_details()

m2 = Manager("Murugan", 41, 75)
m2.show_details()
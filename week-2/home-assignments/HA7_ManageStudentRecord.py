class Student:
    def __init__(self, name, grade, department):
        self.name = name
        self.grade = grade
        self.department = department

    def print_info(self):
        print(f"Name: {self.name}, Grade: {self.grade}, Department: {self.department}")

    def update_grade(self, new_grade):
        self.grade = new_grade


if __name__ == "__main__":
    student1 = Student("Alice Johnson", "A", "Computer Science")
    student2 = Student("Bob Smith", "B", "Mechanical Engineering")
    student3 = Student("Carol Lee", "C", "Electrical Engineering")

    students = [student1, student2, student3]

    print("Initial student information:")
    for student in students:
        student.print_info()

    print("\nUpdating grade of Bob Smith to A+")

    student2.update_grade("A+")

    print("\nUpdated student information:")
    for student in students:
        student.print_info()

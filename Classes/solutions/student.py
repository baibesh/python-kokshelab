class Student:
    def __init__(
        self,
        name: str,
        grades: list = [],
    ):
        self.name = name
        self.grades = grades

    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_average(self):
        if len(self.grades) == 0:
            return 0

        return sum(self.grades) / len(self.grades)

    def has_passed(self):
        if self.calculate_average() >= 50:
            return True

        return False


student1 = Student("Джон Уик")
student1.add_grade(70)
student1.add_grade(80)

print(student1.grades)  # Вывод: [70, 80]
print(student1.calculate_average())  # Вывод: 75.0
print(student1.has_passed())  # Вывод: True

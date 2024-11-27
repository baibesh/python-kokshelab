class Employee:
    def __init__(self, name):
        self.name = name
        self._salary = 0

    # setter
    def set_salary(self, sum):
        self._salary = sum

    # getter
    def get_salary(self):
        return self._salary

    def get_info(self):
        return f"Сотрудник: {self.name}, Зарплата: {self._salary}$"


ivan = Employee("Иван")
print(ivan.get_salary())
ivan.set_salary(1000)
print(ivan.get_salary())
print(ivan.get_info())

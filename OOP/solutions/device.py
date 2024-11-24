class Device:  # Parent class | Super class
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def get_info(self):
        return f"Устройство: {self.brand}, Модель: {self.model}"


class Smartphone(Device):  # Child class
    def __init__(self, brand, model, os):
        self.os = os
        self.brand = brand
        self.model = model

    def get_info(self):
        return f"Устройство: {self.brand}, Модель: {self.model}. Операционная система: {self.os}"


class Laptop(Device):
    def __init__(self, brand, model, ram):
        self.ram = ram
        self.brand = brand
        self.model = model

    def get_info(self):
        return f"Устройство: {self.brand}, Модель: {self.model}. Объем оперативной памяти: {self.ram}"


smartphone = Smartphone(
    brand="Samsung",
    model="S24",
    os="Android",
)
print(smartphone.get_info())

laptop = Laptop(brand="HP", model="RS123", ram="16 GB")
print(laptop.get_info())

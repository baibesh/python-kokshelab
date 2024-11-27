class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def restock(self, sum):
        self.quantity += sum

    def sell(self, sum):
        if self.quantity >= sum:
            self.quantity -= sum


laptop = Product(
    name="Ноутбук",
    price=1000,
    quantity=10,
)

phone = Product(
    name="Телефон",
    price=500,
    quantity=20,
)

phone.sell(18)
print(phone.quantity)  # Вывод: 2

phone.restock(40)
print(phone.quantity)

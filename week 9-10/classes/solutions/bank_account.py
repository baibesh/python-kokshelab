class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, sum):
        self.balance += sum

    def withdraw(self, sum):
        if self.balance >= sum:
            self.balance -= sum
            return f"{sum} снято. остаток: {self.balance}"
        return "Недостаточно средств"


account1 = BankAccount("Алиса", 500)

account1.deposit(200)
print(account1.balance)  # Вывод: 700

print(account1.withdraw(600))
print(account1.balance)

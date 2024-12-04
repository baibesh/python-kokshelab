user_input = input("Введите число: ")

try:
    number = int(user_input)
    print(f"Квадрат числа: {number ** 2}")
except ValueError:
    print("Ошибка: введенное значение не является числом.")

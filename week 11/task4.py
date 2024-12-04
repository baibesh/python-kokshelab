try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    operation = input("Введите операцию (+, -, *, /): ")

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2
    else:
        print("Ошибка: введена неверная операция.")
    print(f"Результат: {result}")
except ValueError:
    print("Ошибка: введено не числовое значение.")
except ZeroDivisionError:
    print("Ошибка: деление на ноль невозможно.")

try:
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    result = num1 / num2
    print(f"Результат деления: {result}")
except ValueError:
    print("Ошибка: введено не число. Пожалуйста, введите корректные числовые значения.")
except ZeroDivisionError:
    print("Ошибка: деление на ноль невозможно. Введите другое значение для второго числа.")

file_name = input("Введите имя файла: ")

try:
    with open(file_name, "r") as file:
        total = 0
        for line in file:
            try:
                total += int(line)
            except ValueError:
                print(f"Предупреждение: строка '{line.strip()}' не является целым числом и будет пропущена.")
        print(f"Сумма всех чисел в файле: {total}")
except FileNotFoundError:
    print("Ошибка: файл не найден.")

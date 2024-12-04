file_name = input("Введите имя файла: ")

try:
    file = open(file_name, "r")
    content = file.read()
    print("Содержимое файла:")
    print(content)
except FileNotFoundError:
    print("Ошибка: файл не найден.")
finally:
    print("Попытка открытия файла завершена.")
    if 'file' in locals() and not file.closed:
        file.close()

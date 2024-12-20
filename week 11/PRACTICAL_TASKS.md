### **Часть 1. Использование `try-except` отдельно**  
**Задача: Преобразование строки в число**  
Напишите программу, которая принимает строку от пользователя и преобразует её в целое число.  
- Если введённое значение нельзя преобразовать, программа должна вывести сообщение об ошибке.  

---

### **Часть 2. Использование `try-except` внутри функции**  
**Задача: Чтение чисел из файла**  
Напишите функцию `read_number_from_file(filename)`, которая открывает файл, читает из него строку и пытается преобразовать её в число.  
- Если файл не найден или строка не является числом, функция возвращает соответствующую ошибку.  

**Примеры:**  
```python

# Пример использования:
print(read_number_from_file("number.txt"))
```

---

### **Часть 3. Использование `try-except` внутри метода**  
**Задача: Обработка данных**  
Создайте класс `DataProcessor` с методом `process`, который принимает список чисел и возвращает их сумму.  
- Если передан не список или элементы не числа, метод должен обработать ошибку.  

**Примеры:**  
```python

# Пример использования:
processor = DataProcessor()
print(processor.process([1, 2, 3]))  # Ожидается: 6
print(processor.process("123"))      # Ожидается: "Ошибка: Некорректный тип данных."
```


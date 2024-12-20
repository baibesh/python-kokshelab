### 1. **Инкапсуляция: Учёт сотрудников**

#### Задача:  
Создайте класс `Employee`, чтобы управлять данными сотрудников.  
- Инкапсулируйте атрибуты:  
  - `_name` – имя сотрудника.  
  - `_salary` – зарплата сотрудника.  
- Методы:  
  - **set_salary(amount)** – устанавливает зарплату (должна быть положительным числом).  
  - **get_salary()** – возвращает текущую зарплату.  
  - **get_info()** – возвращает строку `"Сотрудник: <name>, Зарплата: <salary>"`.  

#### Пример использования:
```python
employee = Employee("Иван", 50000)
print(employee.get_info())  # Вывод: Сотрудник: Иван, Зарплата: 50000
employee.set_salary(60000)  
print(employee.get_info())  # Вывод: Сотрудник: Иван, Зарплата: 60000
employee.set_salary(-1000)  # Вывод: Зарплата должна быть положительным числом
```

---

### 2. **Наследование: Электронные устройства**

#### Задача:  
Создайте базовый класс `Device`, который содержит:  
- Атрибуты:  
  - `brand` – бренд устройства.  
  - `model` – модель устройства.  
- Метод:  
  - **get_info()** – возвращает строку `"Устройство: <brand>, Модель: <model>"`.  

Создайте подклассы:  
1. `Smartphone` с атрибутом `os` (операционная система).  
2. `Laptop` с атрибутом `ram` (объем оперативной памяти).  

Каждый подкласс должен расширить метод **get_info()**, добавляя информацию о своем атрибуте.

#### Пример использования:
```python
phone = Smartphone("Samsung", "Galaxy S23", "Android")
laptop = Laptop("Apple", "MacBook Pro", "16GB")

print(phone.get_info())  # Вывод: Устройство: Samsung, Модель: Galaxy S23, ОС: Android
print(laptop.get_info())  # Вывод: Устройство: Apple, Модель: MacBook Pro, RAM: 16GB
```

---

### 3. **Полиморфизм: Форматирование текста**

#### Задача:  
Создайте базовый класс `TextFormatter` с методом **format(text)**.  
- Создайте подклассы:  
  1. `UppercaseFormatter` – метод **format(text)** возвращает текст в верхнем регистре.  
  2. `LowercaseFormatter` – метод **format(text)** возвращает текст в нижнем регистре.  
  3. `TitlecaseFormatter` – метод **format(text)** возвращает текст с заглавной буквой у каждого слова.  

Создайте функцию, принимающую список форматов и текст, применяя каждый формат.

#### Пример использования:
```python
text = "Привет, Мир!"
formatters = [UppercaseFormatter(), LowercaseFormatter(), TitlecaseFormatter()]

for formatter in formatters:
    print(formatter.format(text))
# Вывод:
# ПРИВЕТ, МИР!
# привет, мир!
# Привет, Мир!
```

---

### 4. **Абстракция: Электронные устройства**

#### Задача:
Создайте абстрактный класс `ElectronicDevice` с абстрактными методами **turn_on()** и **turn_off()**.
Создайте подклассы:
1. `Smartphone` — реализует методы `turn_on()` и `turn_off()`, выводя `"Смартфон включен"` и `"Смартфон выключен"`.
2. `Television` — реализует методы `turn_on()` и `turn_off()`, выводя `"Телевизор включен"` и `"Телевизор выключен"`.

Используйте модуль `abc` для реализации абстрактного класса.

#### Пример использования:
```python
devices = [Smartphone(), Television()]

for device in devices:
    device.turn_on()
    device.turn_off()

# Вывод:
# Смартфон включен
# Смартфон выключен
# Телевизор включен
# Телевизор выключен
```


---

### 5. **Комбинированная задача: Учёт пользователей**

#### Задача A:  
Создайте базовый класс `User`, содержащий:  
- Инкапсулированные атрибуты `_username` и `_email`.  
- Методы:  
  - **get_user_info()** – возвращает `"Имя пользователя: <username>, Email: <email>"`.  

Создайте подклассы:  
1. `AdminUser` – метод **get_user_info()** добавляет `"Роль: Администратор"`.  
2. `GuestUser` – метод **get_user_info()** добавляет `"Роль: Гость"`.  

Напишите функцию, принимающую список пользователей и выводящую их информацию.

#### Пример использования:
```python
admin = AdminUser("admin123", "admin@example.com")
guest = GuestUser("guest456", "guest@example.com")

users = [admin, guest]
for user in users:
    print(user.get_user_info())
# Вывод:
# Имя пользователя: admin123, Email: admin@example.com, Роль: Администратор
# Имя пользователя: guest456, Email: guest@example.com, Роль: Гость
```


#### Задача B:
Создайте базовый класс `Employee` с инкапсулированными атрибутами `__name` и `__salary`.
- **Методы:**
  - **get_name()** — возвращает имя сотрудника.
  - **get_salary()** — возвращает зарплату сотрудника.
  - **set_salary(new_salary)** — устанавливает новую зарплату.

Создайте подклассы:
1. `Developer` — имеет дополнительный атрибут `programming_language` и метод **code()**, выводящий `"Разработка на <programming_language>"`.
2. `Manager` — имеет дополнительный атрибут `team_size` и метод **manage()**, выводящий `"Управление командой из <team_size> человек"`.

Напишите функцию **show_employee_info(employees)**, которая принимает список сотрудников и выводит информацию о каждом, а также вызывает их специфические методы.

#### Пример использования:
```python
dev = Developer("Анна", 80000, "Python")
mgr = Manager("Игорь", 90000, 5)

employees = [dev, mgr]
show_employee_info(employees)

# Вывод:
# Сотрудник: Анна, Зарплата: 80000
# Разработка на Python
# Сотрудник: Игорь, Зарплата: 90000
# Управление командой из 5 человек
```

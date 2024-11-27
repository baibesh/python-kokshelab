### 1. **Система управления задачами**

#### Задача:  
Создайте класс `Task` с атрибутами `title` (название), `description` (описание), и `is_completed` (выполнена ли задача).  
- Добавьте методы:  
  - **complete()** – отмечает задачу как выполненную (`is_completed = True`).  
  - **reopen()** – отмечает задачу как невыполненную (`is_completed = False`).  

#### Пример использования:
```python
task1 = Task("Написать код", "Создать класс Task")
task2 = Task("Протестировать", "Проверить функционал")

print(task1.complete())  # Вывод: "Задача 'Написать код' выполнена"
print(task1.reopen())    # Вывод: "Задача 'Написать код' снова открыта"
```

---

### 2. **Симуляция магазина**

#### Задача:  
Создайте класс `Customer` с атрибутами `name` (имя) и `wallet` (сумма денег).  
- Добавьте методы:  
  - **add_funds(sum)** – пополняет кошелек.  
  - **buy(item_price)** – покупает товар, уменьшая сумму в кошельке (не допускайте отрицательного баланса).  

#### Пример использования:
```python
customer = Customer("Иван", 1000)

customer.add_funds(500)
print(customer.wallet)  # Вывод: 1500

print(customer.buy(2000))  # Вывод: "Недостаточно средств"
print(customer.buy(500))   # Вывод: "Вы купили товар за 500. Остаток: 1000"
```

---


### 3. **Управление книгами пользователей**

#### Задача:  
Создайте класс `UserLibrary` с атрибутами `user` (имя пользователя) и `books` (список прочитанных книг).  
- Добавьте методы:  
  - **add_book(book_title)** – добавляет книгу в список.  
  - **list_books()** – выводит все книги пользователя.  

#### Пример использования:
```python
user_library = UserLibrary(user="Анна", books=[])

user_library.add_book("Война и мир")
user_library.add_book("Преступление и наказание")
print(user_library.list_books())
# Вывод: ["Война и мир", "Преступление и наказание"]
```

---


### 4. **Счетчик посещений**

#### Задача:  
Создайте класс `Counter` с атрибутом `count` (количество посещений).  
- Добавьте методы:  
  - **increment()** – увеличивает счетчик.  
  - **reset()** – сбрасывает счетчик.  

#### Пример использования:
```python
counter = Counter()

counter.increment()
counter.increment()
print(counter.count)  # Вывод: 2

counter.reset()
print(counter.count)  # Вывод: 0
```

---

## OOP

### 1. **Полиморфизм: Форматирование текста**

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
uppercase_formatter = UppercaseFormatter()
lowercase_formatter = LowercaseFormatter()
titlecase_formatter = TitlecaseFormatter()

uppercase_formatter.format(text)
lowercase_formatter.format(text)
titlecase_formatter.format(text)

# Вывод:
# ПРИВЕТ, МИР!
# привет, мир!
# Привет, Мир!
```

---

### 2. **Абстракция: Электронные устройства**

#### Задача:
Создайте абстрактный класс `ElectronicDevice` с абстрактными методами **turn_on()** и **turn_off()**.
Создайте подклассы:
1. `Smartphone` — реализует методы `turn_on()` и `turn_off()`, выводя `"Смартфон включен"` и `"Смартфон выключен"`.
2. `Television` — реализует методы `turn_on()` и `turn_off()`, выводя `"Телевизор включен"` и `"Телевизор выключен"`.

Используйте модуль `abc` для реализации абстрактного класса.

#### Пример использования:
```python
devices = [Smartphone(), Television()]

smartphone = Smartphone()
smartphone.turn_on()
smartphone.turn_off()


television = Television()
television.turn_on()
television.turn_off()

    
# Вывод:
# Смартфон включен
# Смартфон выключен
# Телевизор включен
# Телевизор выключен
```


---

### 4. **Комбинированная задача: Учёт пользователей**

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

admin.get_user_info()
guest.get_user_info()

# Вывод:
# Имя пользователя: admin123, Email: admin@example.com, Роль: Администратор
# Имя пользователя: guest456, Email: guest@example.com, Роль: Гость
```
---

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

---

class Book:
    """
    title
    author
    is_available
    """

    def __init__(self, title, author, is_available=True):
        self.title = title
        self.author = author
        self.is_available = is_available

    def borrow(self):
        if not self.is_available:
            return f"Книга: {self.title} недоступна"
        self.is_available = False
        return f"Вы взяли книгу: {self.title}"

    def return_book(self):
        self.is_available = True
        return f"Книга: {self.title} была возвращена"


book1 = Book(
    title="Гарри Поттер",
    author="Дж.К. Роулинг",
)

print(book1.borrow())
print(book1.return_book())
print(book1.borrow())

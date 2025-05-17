from typing import List
from book import Book  # импортируем тип Book

class User:
    def __init__(self, name: str):
        self.name: str = name
        self.id: str = name.lower().replace(" ", "_")  # простой ID
        self.borrowed_books: List[Book] = []  # список книг, взятых пользователем

    def borrow_book(self, book: Book) -> None:
        if book is None or not isinstance(book, Book):
            print("\n❌ Ошибка: Передан некорректный объект вместо книги.")
            return
        # Проверка: пользователь уже взял 3 книги
        if len(self.borrowed_books) >= 3:
            print(f"\n🚫 Пользователь {self.name} не может взять больше 3 книг.")
            return

        # Проверка: книга доступна
        if not book.is_available:
            print(f"\n❌ Книга '{book.title}' недоступна.")
            return

        # Добавляем книгу пользователю
        self.borrowed_books.append(book)
        book.is_available = False
        print(f"\n✅ Пользователь {self.name} взял книгу '{book.title}'.")

        #Пользователь возвращает книгу в библиотеку
    def return_book(self, book: Book) -> None:
        if book is None or not isinstance(book, Book):
            print("\n❌ Ошибка: Передан некорректный объект вместо книги.")
            return
        
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.is_available = True
            print(f"\n✅ Пользователь {self.name} вернул книгу '{book.title}'.")
        else:
            print(f"\n❌ Пользователь {self.name} не взял книгу '{book.title}'.")
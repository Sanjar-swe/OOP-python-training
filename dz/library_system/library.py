from typing import List, Dict
from book import Book
from user import User

class Library:
    def __init__(self):
        self.books: List[Book] = []
        self.users: Dict[str, User] = {}

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def add_user(self, user: User) -> None:
        self.users[user.id] = user

    def borrow_book(self, user_id: str, book_title: str) -> None:
        if user_id not in self.users:
            print(f"Пользователь с ID {user_id} не найден.")
            return

        book = next((b for b in self.books if b.title == book_title), None)

        if book is None:
            print(f"Книга с названием '{book_title}' не найдена.")
            return

        user = self.users[user_id]
        user.borrow_book(book)

    def show_all_books(self) -> None:
        for book in self.books:
            print(book.title)

    def show_all_users(self) -> None:
        for user in self.users.values():
            print(user.id)

    def sort_books(self, by: str = "price") -> None:
        if by == "price":
            self.books.sort(key=lambda b: b.price)
        elif by == "author":
            self.books.sort(key=lambda b: b.author)
        else:
            print("Неверный параметр сортировки.")
            return
    
    def return_book(self, user_id: str, book_title: str):
        if user_id not in self.users:
            print(f"Пользователь с ID {user_id} не найден.")
            return
        book = next((b for b in self.books if b.title == book_title), None)
        if book is None:
            print(f"Книга с названием '{book_title}' не найдена.")
            return
        user = self.users[user_id]
        user.return_book(book)
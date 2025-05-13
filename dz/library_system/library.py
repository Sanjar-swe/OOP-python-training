from book import Book
from user import User

class Library:
    def __init__(self):
        self.books = []  # Список всех книг
        self.users = {}  # Словарь пользователей {user_id: User}
        
    def add_book(self, book: Book):
        self.books.append(book)
        
    def add_user(self, user_id: str, user: User):
        self.users[user_id] = user
    
    def borrow_book(self, user_id: str, book_title: str):
        if user_id not in self.users:
            print(f"Пользователь с ID {user_id} не найден.")
            return
        
        book = next((b for b in self.books if b.title == book_title), None)
        if book is None:
            print(f"Книга '{book_title}' не найдена.")
            return
        
        user = self.users[user_id]
        user.borrow_book(book)
        
    def show_all_books(self):
        for book in self.books:
            print(f"{book.title} - {book.author} - ${book.price} - {'Доступна' if book.is_available else 'Недоступна'}")
    
    def show_all_users(self):
        for user_id, user in self.users.items():
            print(f"{user_id}: {user.name}")
    
    def sort_books(self, by="price"):
        if by == "price":
            self.books.sort(key=lambda b: b.price)
        elif by == "author":
            self.books.sort(key=lambda b: b.author)
        else:
            print("Неверный параметр сортировки. Используй 'price' или 'author'.")

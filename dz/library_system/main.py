# main.py
from book import Book
from user import User
from library import Library

# создаём библиотеку
lib = Library("Центральная библиотека")

# создаём книги
book1 = Book("1984", "George Orwell", 9.99)
book2 = Book("Brave New World", "Aldous Huxley", 8.99)
book3 = Book("Fahrenheit 451", "Ray Bradbury", 7.99)

# добавляем книги в библиотеку
lib.add_book(book1)
lib.add_book(book2)
lib.add_book(book3)

# создаём пользователя
user1 = User("Alice Johnson")
user2 = User("Bob Smith")
user3 = User("Charlie Brown")


# добавляем пользователя в библиотеку
lib.add_user(user1)
lib.add_user(user2)
lib.add_user(user3)

# пользователь берёт книгу
lib.borrow_book(user1.id, "1984")

# книги оставшиеся в библиотеке
print("\n📚 Оставшиеся Книги в библиотеке после выдачи:")
lib.show_all_books()

# показать все книги
print("\n📚 Все книги:")
lib.show_all_books()

# показать всех пользователей
print("\n👤 Все пользователи:")
lib.show_all_users()

# сортировка книг
print("\n📚 Сортировка книг по цене:")
lib.sort_books(by="price")
lib.show_all_books()

print("\n📚 Сортировка книг по автору:")
lib.sort_books(by="author")
lib.show_all_books()



# пользователь возвращает книгу
lib.borrow_book(user1.id, "1984")
user1.return_book(book1)
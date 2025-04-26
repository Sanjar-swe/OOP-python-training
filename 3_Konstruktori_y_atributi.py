# ✅ **ШАГ 3: Конструкторы (`__init__`) и атрибуты**

# **Задача 3: "Класс Книга"**  
# Создай класс `Book`, который при создании принимает:
# - название
# - автора
# - количество страниц

# Добавь метод `description()`, который возвращает строку с описанием книги.

# **Зачем:** Чтобы понять, как правильно **создавать объекты** с разными данными.

# ---

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        
    def description(self):
        return f"{self.title} by {self.author}, {self.pages} pages"
    
book = Book("The Great Gatsby", "F. Scott Fitzgerald", 208)
print(book.description())
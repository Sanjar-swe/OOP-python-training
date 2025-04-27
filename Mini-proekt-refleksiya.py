class Book:
    def __init__(self, title, author, pages, year):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year
        
    def description(self):
        return f"{self.title} by {self.author}, {self.pages} pages"

class Library:
  def __init__(self):
    self._books = []
    
  def add_book(self, book):
    self._books.append(book)
  
  def find_book(self, title):
    # self.title.find(title)
    for book in self._books:
      if book.title == title:
        return book
    return None #if book not exists
    
  def display_books(self):
    if not self._books:
      print("Library is empty")
    else:
      for book in self._books:
        print(book.description())
        
  def remove_book(self, title):
    for book in self._books:
      if book.title == title:
        self._books.remove(book)
        return True
    return False

library = Library()

book1 = Book("The Hobbit", "J.R.R. Tolkien", 310, 1937)
book2 = Book("1984", "George Orwell", 328, 1949)

library.add_book(book1)
library.add_book(book2)

library.display_books()

found = library.find_book("The Hobbit")

if found:
  print(found.description())
else:
  print("Book not found")
  
library.remove_book("The Hobbit")
print("After removing: 'The Hobbit'")
library.display_books()
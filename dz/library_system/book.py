class Book:
    def __init__(self, title: str, author: str, price: float):
        self.title: str = title
        self.author: str = author
        self.price: float = price
        self.is_available: bool = True
class Book:
    def __init__(self, title: str, author: str, price: float):
        if price < 0:
            raise ValueError("Цена книги не может быть отрицательной")
        if price > 1_000_000:
            raise ValueError("Цена книги не может превышать 1 000 000")
        self.title: str = title
        self.author: str = author
        self.price: float = price
        self.is_available: bool = True
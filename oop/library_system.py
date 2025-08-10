class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        print(f"Deleting {self.title}")

    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"


class EBook(Book):
    def __init__(self, title: str, author: str, year: int, file_size: int):
        super().__init__(title, author, year)
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, published in {self.year}, File Size: {self.file_size}KB"

    def __repr__(self):
        return f"EBook('{self.title}', '{self.author}', {self.year}, {self.file_size})"


class PrintBook(Book):
    def __init__(self, title: str, author: str, year: int, page_count: int):
        super().__init__(title, author, year)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, published in {self.year}, Page Count: {self.page_count}"

    def __repr__(self):
        return f"PrintBook('{self.title}', '{self.author}', {self.year}, {self.page_count})"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book)
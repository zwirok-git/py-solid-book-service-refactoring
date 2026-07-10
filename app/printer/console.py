from app.book import Book
from app.printer.base import BasePrinter


class ConsolePrinter(BasePrinter):
    def print(self, book: Book):
        print(f"Printing the book: {book.title}...")
        print(book.content)

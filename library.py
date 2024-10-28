from book import Book
from member import Member
from transaction import Transaction

class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.transactions = []

    def add_book(self, book):
        self.books.append(book)

    def register_member(self, member):
        self.members.append(member)

    def borrow_book(self, member_id, isbn):
        member = next((m for m in self.members if m.member_id == member_id), None)
        book = next((b for b in self.books if b.isbn == isbn), None)

        if member and book and book.borrow():
            transaction = Transaction(member, book, 'borrow')
            self.transactions.append(transaction)
            print(transaction)
        else:
            print(f"Cannot borrow the book: {book} (Available: {not book.is_borrowed})")

    def return_book(self, member_id, isbn):
        member = next((m for m in self.members if m.member_id == member_id), None)
        book = next((b for b in self.books if b.isbn == isbn), None)

        if member and book:
            book.return_book()
            transaction = Transaction(member, book, 'return')
            self.transactions.append(transaction)
            print(transaction)
        else:
            print("Return transaction failed.")

from library import Library
from book import Book
from member import Member

def main():
    library = Library()

    # Adding books
    book1 = Book("1984", "George Orwell", "1234567890")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "0987654321")
    library.add_book(book1)
    library.add_book(book2)

    # Registering members
    member1 = Member("Alice", "001")
    member2 = Member("Bob", "002")
    library.register_member(member1)
    library.register_member(member2)

    # Borrowing and returning books
    library.borrow_book("001", "1234567890")  # Alice borrows "1984"
    library.return_book("001", "1234567890")  # Alice returns "1984"

    library.borrow_book("002", "0987654321")  # Bob borrows "To Kill a Mockingbird"
    library.borrow_book("002", "1234567890")  # Bob tries to borrow "1984"

if __name__ == "__main__":
    main()

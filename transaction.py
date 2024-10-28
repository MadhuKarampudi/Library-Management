class Transaction:
    def __init__(self, member, book, action):
        self.member = member
        self.book = book
        self.action = action  # 'borrow' or 'return'
        self.transaction_id = id(self)

    def __str__(self):
        return f"Transaction ID: {self.transaction_id}, {self.action} '{self.book}' by {self.member}"

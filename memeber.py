class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id

    def __str__(self):
        return f"{self.name} (ID: {self.member_id})"

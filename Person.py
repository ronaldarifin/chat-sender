class Person:
    def __init__(self, name, phone, tags=[]):
        self.name = name
        self.phone = phone
        self.tags = tags

    def __repr__(self):
        return f"{self.name}'s phone is {self.phone} and considered a {self.tags}"

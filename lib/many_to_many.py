class Author:
    def __init__(self, name):
        self.name = name

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return list(set([contract.book for contract in self.contracts()]))

    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        return contract

    def total_royalties(self):
        return sum([contract.royalties for contract in self.contracts()])


class Book:
    def __init__(self, title):
        self.title = title

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return list(set([contract.author for contract in self.contracts()]))


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise TypeError("author must be an instance of Author")
        if not isinstance(book, Book):
            raise TypeError("book must be an instance of Book")
        if not isinstance(date, str):
            raise TypeError("date must be a string")
        if not isinstance(royalties, int):
            raise TypeError("royalties must be an integer")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        self.__class__.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return sorted([contract for contract in cls.all if contract.date == date], key=lambda x: x.date)

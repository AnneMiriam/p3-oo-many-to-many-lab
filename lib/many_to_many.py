class Author:
    all = []
    # Author class initializes with name
    def __init__(self, name):
        self.name = name
        Author.all.append(self)
    # Author class has method contracts() that returns a list of its contracts
    def contracts(self):
        return [contract for contract in Contract.all if contract.author is self]
    # Author class has method books() that returns a list of its books
    def books(self):
        return [contract.book for contract in self.contracts()]
    # Author class has method sign_contract() that creates a contract for an author and book
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    # Author class has method total_royalties that gets the sum of all its related contracts' royalties
    def total_royalties(self):
        return sum([contract.royalties for contract in self.contracts()])

class Book:
    all = []
    # Book class initializes with title
    def __init__(self, title):
        self.title = title
        Book.all.append(self)
    # Book class has method contracts() that returns a list of its contracts    
    def contracts(self):
        return [contract for contract in Contract.all if contract.book is self]
    # Book class has method authors() that returns a list of its authors
    def authors(self):
        return [contract.author for contract in self.contracts()]


class Contract:
    all = []
    # Contract class initializes with author, book, date, royalties
    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date 
        self.royalties = royalties
        Contract.all.append(self)
    # Contract class validates author of type Author 
    @property
    def author(self):
        return self._author
    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise Exception
    # Contract class validates book of type Book
    @property
    def book(self):
        return self._book
    @book.setter
    def book(self, book):
        if isinstance(book, Book):
            self._book = book
        else:
            raise Exception
     
    # Contract class validates date of type str
    @property
    def date(self):
        return self._date
    @date.setter
    def date(self, date):
        if isinstance(date, str):
            self._date = date
        else:
            raise Exception
    # Contract class validates royalties of type int - Failed: DID NOT RAISE <class 'Exception'>
    @property
    def royalties(self):
        return self._royalties
    @royalties.setter
    def royalties(self, royalties):
        if isinstance(royalties, int):
            self._royalties = royalties
        else:
            raise Exception
    # Contract class has method contracts_by_date() that sorts all contracts by date
    @classmethod   
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]
import random
import datetime

from source import LibraryItem
from source.Person import Person


def generate_id():
    gen = random.randint(100000, 999999)
    return gen


class User(Person):
    loaned_books = []
    def __init__(self, first_name: str, last_name: str, pesel: int, email:str):
        self.first_name = first_name
        self.last_name = last_name
        self.pesel = pesel
        self.email = email
        self.id = generate_id()

    def loan(self, book: LibraryItem):
        if book.is_loaned == False:
            book.is_loaned = True
            self.loaned_books.append(book)
            book.who_loaned = self
            book.loan_date = datetime.date.today()
            print('Książka została wypożyczona')
        else:
            print('Książka niedostępna')

    def give_back(self, book: LibraryItem):
        if book.is_loaned:
            book.is_loaned = False
            book.loan_date = None
            self.loaned_books.pop(self.loaned_books.index(book))
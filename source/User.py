import random
import datetime

from LibraryItem import LibraryItem
from Person import Person
from termcolor import colored


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

    def books_loaned(self):
        if len(self.loaned_books) == 0:
            print('Nie masz wypożyczonych książek.')
        for book in self.loaned_books:
            print(f'Książka {book.title} autorstwa {book.author.first_name} {book.author.last_name} wypożyczona {book.loan_date}.')
            if book.is_overdue:
                print(colored('Termin zwrotu książki minął!', 'red'))

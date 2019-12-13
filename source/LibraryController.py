from Author import Author
from LibraryItem import LibraryItem
from User import User
from termcolor import colored


class LibraryController:

    books = []
    users = []

    def __init__(self, library_name:str):
        self.library_name = library_name

    def add_book(self, title:str, author:Author, isbn:str):
        title = title.title()
        book = LibraryItem(title, author, isbn)
        self.books.append(book)
        print(f'Do księgozbioru dodano książkę {title} autora {author.first_name} o numerze isbn {isbn}. ')
        return book

    def add_user(self, first_name: str, last_name: str, pesel: int, email:str):
        user = User(first_name, last_name, pesel, email)
        self.users.append(user)
        print(f'Dodano użytkownika {first_name} {last_name}.')
        return user

    def search_book(self, book_name):
        book_name = book_name.title()
        for book in self.books:
            if book.title == book_name:
               # print(f'Znaleziono książkę: {book.title} autorstwa {book.author.last_name} {book.author.first_name}')
                return book

    def search_user_name(self, name):
        name = name.title()
        for user in self.users:
            if user.first_name == name or user.last_name == name or user.first_name + ' ' + user.last_name == name:
                print(f"Znaleziono uzytkownika {user.first_name} o numerze id {user.id}")
                return user

    def search_user_id(self, id):
        id = int(id)
        for user in self.users:
            if user.id == id:
                print(f"Znaleziono uzytkownika {user.first_name} {user.last_name} o numerze id {user.id}")
                return user
        print('Nie znaleziono użytkownika o takim id.')
        return None

    def check_if_loaned(self, title):
        book = self.search_book(title)
        if book.is_loaned:
            print(colored(f'Książka jest wypożyczona przez {book.who_loaned.first_name} {book.who_loaned.last_name} w dniu {book.loan_date}', 'red'))
            if book.is_overdue:
                print(colored('Termin zwrotu książki minął!', 'red'))
        else:

            print(colored('Książka jest dostępna do wypożyczenia', 'green'))

    def users_list(self):
        if len(self.users) == 0:
            print('Nie ma nikogo na liście')
        else:
            for user in self.users:
                print(f'{user.first_name} {user.last_name}, ID: {user.id}, e-mail: {user.email}, pesel: {user.pesel}')

    def books_list(self):
        if len(self.books) == 0:
            print('Brak książek na liście')
        else:
            for book in self.books:
                print(f'{book.title} autorstwa {book.author.first_name} {book.author.last_name}, ISBN: {book.isbn}. ')
                self.check_if_loaned(book.title)
                if book.is_overdue:
                    print(colored('Termin zwrotu książki minął!', 'red'))

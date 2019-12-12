from source import Author
from source.LibraryItem import LibraryItem
from source.User import User


class LibraryControler:

    books = []
    users = []

    def __init__(self, library_name:str):
        self.library_name = library_name

    def add_book(self, title:str, author:Author, isbn:str):
        title.title()
        book = LibraryItem(title, author, isbn)
        self.books.append(book)
        print(f'Do księgozbioru dodano książkę {title} autora {author.first_name} o numerze isbn {isbn}. ')
        return book

    def add_person(self, first_name: str, last_name: str, pesel: int, email:str):
        user = User(first_name, last_name, pesel, email)
        self.users.append(user)
        print(f'Dodano użytkownika {first_name} {last_name}.')
        return user


    def search_book(self, title):
        title = title.title()
        print(f'Przeszukiwanie księgozbioru w poszukiwaniu książki o tytule {title}')
        for book in self.books:
            if book.title == title:
                print(f'Znaleziono książkę: {book.title} autorstwa {book.author.last_name} {book.author.first_name}')
                return book

    def search_user_name(self, name):
        name = name.title()
        for person in self.users:
            if person.first_name == name or person.last_name == name or person.first_name + ' ' + person.last_name == name:
                print(f"Znaleziono uzytkownika {person.first_name} o numerze id {person.id}")

    def check_if_loaned(self, title):
        book = self.search_book(title)
        if book.is_loaned:
            print(f'Książka jest wypożyczona przez {book.who_loaned.first_name} {book.who_loaned.last_name} w dniu {book.loan_date}')
        else:
            print('Książka jest dostępna do wypożyczenia')

    def users_list(self):
        for person in self.users:
            print(f'{person.first_name} {person.last_name}, ID: {person.id}, e-mail: {person.email}, pesel: {person.pesel}')


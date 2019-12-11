from Author import Author
from LibraryItem import LibraryItem


class LibraryControler:

    books = []

    def __init__(self, library_name:str):
        self.library_name = library_name

    def add_book(self, title:str, author:Author, isbn:str):
        book = LibraryItem(title, author, isbn)
        self.books.append(book)
        print(f'Do księgozbioru dodano książkę {title} autora {author.first_name} o numerze isbn {isbn}. ')

    def search_book(self, title):
        print(f'Przeszukiwanie księgozbioru w poszukiwaniu książki o tytule {title}')
        for book in self.books:
            if book.title == title:
                print(f'Znaleziono książkę: {book.title} autorstwa {book.author.last_name} {book.author.first_name}')
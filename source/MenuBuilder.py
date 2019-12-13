import time
import os
import sys
from termcolor import colored
from LibraryController import LibraryController as LC
from LibraryItem import LibraryItem
from Person import Person
from User import User
import DemoData


clear = lambda: os.system('cls')
main_menu = ['1. Obsługa czytelnika', '2. Obsługa bibliotekarza', '3. Wgraj demonstracyjne dane', '4. Wyjdź']
user_menu = ['1. Moje dane', '2. Sprawdź wypożyczone ksiązki', '3. Wypożycz książkę', '4. Zwróć książkę', '5. Cofnij']
librarian_menu = ['1. Lista użytkowników', '2. Lista książek', '3. Dodaj książkę', '4. Dodaj czytelnika', '5. Cofnij']
biblioteka = LC('Biblioteka')



def main_m():
    clear()
    print_main_m()
    main_m_contr()


def print_main_m():
    print(colored("""System biblioteczny
    
    """, 'green'))

    for item in main_menu:
        print(main_menu[main_menu.index(item)])
        time.sleep(0.3)
    print('\n')


def main_m_contr():
    c = input('Podaj wybór: ')
    if c == '1':
        user_m()
    elif c == '2':
        librarian_m()
    elif c == '3':
        load_demo()
    elif c == '4':
        sys.exit()
    else:
        print(colored('Nieprawidłowy wybór!', 'red'))
        time.sleep(2)
        main_m()


def load_demo():
    DemoData.add_demo_users(biblioteka)
    DemoData.add_demo_books(biblioteka)
    print(colored('Załadowano pomyślnie!', 'green'))
    time.sleep(1)
    main_m()


def user_m():
    clear()
    print_user_m()
    user_m_contr()


def print_user_m():
    print(colored("""System biblioteczny

    """, 'green'))
    for item in user_menu:
        print(user_menu[user_menu.index(item)])
    print('\n')


def set_login(is_logged):
    is_logged = True


def check_user():
        id = int(input('Podaj swoje ID:'))
        user = biblioteka.search_user_id(id)
        if user == None:
            print('Nie ma takiego uzytkownika!')
            time.sleep(2)
            main_m()
        return user


def user_m_contr():
    user = check_user()
    n = input('Podaj wybór: ')
    if n == '1':
        user_get_user(user)
    elif n == '2':
        user_check_loan(user)
    elif n == '3':
        user_loan_book(user)
    elif n == '4':
        user_give_back(user)
    elif n == '5':
        main_m()
    else:
        print(colored('Nieprawidłowy wybór!', 'red'))
        time.sleep(2)
        user_m()


def user_get_user(user: User):
    print(f'''    Imię: {user.first_name}
    Nazwisko: {user.last_name}
    Pesel: {user.pesel}
    Email: {user.email}
    ID: {user.id}''')
    confirm()
    back_to_menu(1)


def user_check_loan(user: User):
    user.books_loaned()
    confirm()
    back_to_menu(1)


def user_loan_book(user: User):
    book = input('Podaj nazwę książki:')
    user.loan(biblioteka.search_book(book))
    confirm()
    back_to_menu(1)


def user_give_back(user: User):
    book = input('Podaj nazwę książki:')
    user.give_back(biblioteka.search_book(book))
    confirm()
    back_to_menu(1)


def librarian_m():
    clear()
    print_librarian_m()
    librarian_m_contr()


def print_librarian_m():
    print(colored("""System biblioteczny

    """, 'green'))
    for item in librarian_menu:
        print(librarian_menu[librarian_menu.index(item)])
    print('\n')

def librarian_m_contr():
    n = input('Podaj wybór: ')
    if n == '1':
        librarian_get_users()
    elif n == '2':
        librarian_get_books()
    elif n == '3':
        librarian_add_book()
    elif n == '4':
        librarian_add_user()
    elif n == '5':
        main_m()
    else:
        print(colored('Nieprawidłowy wybór!', 'red'))
        time.sleep(2)
        librarian_m()


def librarian_get_users():
    biblioteka.users_list()
    confirm()
    back_to_menu(2)


def librarian_get_books():
    biblioteka.books_list()
    confirm()
    back_to_menu(2)


def librarian_add_book():
    title = input('Podaj tytuł: ')
    author_name = input('Podaj imię autora: ')
    author_lastname = input('Podaj nazwisko autora: ')
    isbn = input('Podaj numer isbn książki: ')
    biblioteka.add_book(title, Person(author_name, author_lastname), isbn)
    confirm()
    back_to_menu(2)


def librarian_add_user():
    first_name = input('Podaj imię: ')
    last_name = input('Podaj nazwisko: ')
    pesel = int(input('Podaj pesel: '))
    email = input ('Podaj email: ')
    biblioteka.add_user(first_name, last_name, pesel, email)
    confirm()
    back_to_menu(2)


def confirm():
    input('Naciśnij enter, by kontynuować')


def back_to_menu(i):
    if i == 1:
        user_m()
    elif i == 2:
        librarian_m()
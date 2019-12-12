import random

from source.LibraryControler import LibraryControler
from source.Person import Person

biblioteka = LibraryControler('biblioteczken')

biblioteka.add_person('Przemek', 'Mikulski', 9505281111, 'sads@adsd.pl')
prz = biblioteka.add_person('Przemek', 'Miwewqr', 95342535111, 'sads@adsd.pl')

book1 = biblioteka.add_book("Miecz Przeznaczenia", Person('Andrzej', 'Sapkowski'), str(random.randint(1000000000000, 9999999999999)))

biblioteka.search_book('Miecz Przeznaczenia')

biblioteka.search_user_name('Przemek')

prz.loan(biblioteka.search_book('Miecz Przeznaczenia'))

print(book1.who_loaned.first_name)
print(book1.loan_date)
print(f'lol  {book1.between_time()}')
biblioteka.check_if_loaned('miecz przeznaczenia')
print(len(prz.loaned_books))
prz.give_back(biblioteka.search_book('Miecz Przeznaczenia'))
print(len(prz.loaned_books))
biblioteka.check_if_loaned('miecz przeznaczenia')

print(book1.between_time())
biblioteka.users_list()
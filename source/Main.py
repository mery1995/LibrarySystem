from LibraryControler import LibraryControler
from Person import Person
from LibraryItem import LibraryItem
from User import User


import random

biblioteka = LibraryControler('biblioteczken')

pszemek = User('Przemek', 'Mikulski', 950528111, 'mail@mail.com')
print(pszemek.get_id())

biblioteka.add_book("Miecz Przeznaczenia", Person('Andrzej', 'Sapkowski'), str(random.randint(1000000000000, 9999999999999)))

biblioteka.search_book('Miecz Przeznaczenia')
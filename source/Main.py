from LibraryControler import LibraryControler
from Person import Person
from LibraryItem import LibraryItem


biblioteka = LibraryControler('biblioteczken')

biblioteka.add_book("Miecz Przeznaczenia", Person('Andrzej', 'Sapkowski'), '1234567')

biblioteka.search_book('Miecz Przeznaczenia')
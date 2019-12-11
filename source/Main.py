from source.LibraryControler import LibraryControler
from source.Person import Person
from source.LibraryItem import LibraryItem


biblioteka = LibraryControler('biblioteczken')

biblioteka.add_book("Miecz Przeznaczenia", Person('Andrzej', 'Sapkowski'), '1234567')

biblioteka.search_book('Miecz Przeznaczenia')
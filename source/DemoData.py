
from Person import Person
import random
#Adding users


def add_demo_users(biblioteka):
    biblioteka.add_user('Przemek', 'Nowak', 95435633422,'example@example.com')
    biblioteka.add_user('Adam', 'Pawełczak', 95041342832, 'example@example.com')
    biblioteka.add_user('Maciej', 'Wojtyła', 9683724832, 'example@example.com')
    biblioteka.add_user('Elżbieta', 'Kowalska', 95040294832, 'example@example.com')
    biblioteka.add_user('Marcin', 'Buczyński', 95040294832, 'example@example.com')
    biblioteka.add_user('Marysia', 'Hel', 95040294832, 'example@example.com')
    biblioteka.add_user('Alicja', 'Konieczna', 95040294832, 'example@example.com')
    biblioteka.add_user('Kazimierz', 'Piekarski', 95040294832, 'example@example.com')
    biblioteka.add_user('Asia', 'Nowakiewicz', 95040294832, 'example@example.com')
    biblioteka.add_user('Marcel', 'Nowakierski', 95040294832, 'example@example.com')

def add_demo_books(biblioteka):
    biblioteka.add_book("Miecz Przeznaczenia", Person('Andrzej', 'Sapkowski'), str(random.randint(1000000000000, 9999999999999)))
    biblioteka.add_book("Ojciec chrzestny", Person('Mario', 'Puzo'), str(random.randint(1000000000000, 9999999999999)))
    biblioteka.add_book("Władca Pierścieni", Person('J. R. R.', 'Tolkien'), str(random.randint(1000000000000, 9999999999999)))
    biblioteka.add_book("Hrabia Monte Christo", Person('Aleksander', 'Dumas'), str(random.randint(1000000000000, 9999999999999)))
    biblioteka.add_book("Sherlock Holmes TOM 1", Person('Arthur Conan', 'Doyle'), str(random.randint(1000000000000, 9999999999999)))
    biblioteka.add_book("Harry Potter i Komnata Tajemnic", Person('J. K.', 'Rowling'), str(random.randint(1000000000000, 9999999999999)))


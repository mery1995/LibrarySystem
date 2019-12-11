from Person import Person
import random

def generate_id():
    gen = random.randint(100000, 999999)
    return gen


class User(Person):
    pesel = 0
    email = ''
    id = 0

    def __init__(self, first_name: str, last_name: str, pesel: int, email:str):
        self.first_name = first_name
        self.last_name = last_name
        self.pesel = pesel
        self.email = email
        self.id = generate_id()

    def get_id(self):
        return self.id

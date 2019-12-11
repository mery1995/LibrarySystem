from source.Person import Person


class User(Person):
    pesel = 0
    email = ''

    def __init__(self, first_name: str, last_name: str, pesel: int, email:str):
        self.first_name = first_name
        self.last_name = last_name
        self.pesel = pesel
        self.email = email
from source.Person import Person


class Author(Person):
    def __init__(self, first_name: str, last_name: str):
        super().__init__(first_name, last_name)
        self.first_name = first_name
        self.last_name = last_name

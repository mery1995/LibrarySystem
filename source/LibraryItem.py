class LibraryItem:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.duration = 30
        self.loanedPtr = ''

    def get_title(self):
        return self.title

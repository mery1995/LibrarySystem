class LibraryItem:
    def __init__(self, title, author, isbn, chapters):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.chapters = chapters
        self.duration = 30
        self.loanedPtr = ''

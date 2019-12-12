import datetime


class LibraryItem:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.duration = 3
        self.is_loaned = False
        self.who_loaned = None
        self.loan_date = None
        self.is_overdue = False

    def between_time(self):
        if self.is_loaned:
            f_date = datetime.date.today()
            l_date = self.loan_date
            if (f_date-l_date).days > self.duration:
                self.is_overdue = True
            else:
                self.is_overdue = False
            return (f_date-l_date).days
        else:
            return 'Książka nie została jeszcze wypożyczona'

import datetime

class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def get_age(self):
        current_year = datetime.datetime.now().year
        return current_year - self.publication_year

book1 = Book("Python Basics", "John Doe", 2015)

print("Book Age:", book1.get_age(), "years")
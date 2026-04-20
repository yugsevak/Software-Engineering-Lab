# Library Book Counter

class Library:
    def __init__(self):
        self.total_books = 5

    def show_books(self):
        print("Total books in library:", self.total_books)

    def add_book(self):
        self.total_books += 1
        print("Book added")

    def remove_book(self):
        if self.total_books > 0:
            self.total_books -= 1
            print("Book removed")
        else:
            print("No books available")

# Create object
lib = Library()

lib.show_books()
lib.add_book()
lib.show_books()
lib.remove_book()
lib.show_books()

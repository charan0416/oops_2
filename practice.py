class Library:

    def __init__(self, name):
        self.name = name
        self.book = []  # Initialize with an empty list to store books

    def add_book(self, book):
        self.book.append(book)  # Add the book to the list
        print(f"Book '{book}' added successfully to {self.name}.")

    def remove_book(self, book):
        if book in self.book:
            self.book.remove(book)
            print(f"Book '{book}' removed successfully from {self.name}.")
        else:
            print(f"Book '{book}' not found in {self.name}.")

    def display_books(self):
        if self.book:
            print(f"Books in {self.name}: {', '.join(self.book)}")
        else:
            print(f"No books in {self.name} currently.")


book1 = Library("Charan Library")
book2 = Library("Devi Library")


book1.add_book("Baru")
book2.add_book("Sriya")


book1.display_books()
book2.display_books()


book1.remove_book("Baru")
book2.remove_book("Nonexistent Book")

book1.display_books()
book2.display_books()

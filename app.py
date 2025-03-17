# from itertools import product
# from tkinter.font import names


class Library:

    def __init__(self,name):
        self.name= name
        self.book = []

    def add_book(self,book,name):
        self.names = name
        self.books = book
        print(f"name:{self.name},book:{self.book} added successfully")

    def remove_book(self,book):
        if book in self.book:
            self.book.remove(book)
            print(f"name:{self.name},book:{self.book} removed successfully")

    def display_books (self):
        if self.book:
            print(f"name:{self.name},book:{self.book}")


book1=Library("charan")
book2=Library("devi")

book1.add_book("Baru")
book2.add_book("sriya")



Library.display_books(book2)
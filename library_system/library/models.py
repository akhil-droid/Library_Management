from django.db import models
from django.http import JsonResponse
from django.views import View

# Define the Book model to represent books in the library system
class Book(models.Model):
    # Title of the book
    title = models.CharField(max_length=200)
    # Author of the book
    author = models.CharField(max_length=100)
    # ISBN of the book, it is unique
    isbn = models.CharField(max_length=13, unique=True)

    # Method to display the book's info in a readable format
    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"

    def __str__(self):
        return self.title

# Define the Library model to represent a collection of books
class Library(models.Model):
    # To store multiple books in a library we have Many-to-many relationship
    books = models.ManyToManyField(Book)

    # Method to add a book to the library
    def add_book(self, book):
        self.books.add(book)
        self.save()

    # Method to display information for all books in the library
    def display_all_books(self):
        return [book.display_info() for book in self.books.all()]
    
    # Method to search for books by title in the library using filter queryset
    def search_by_title(self, title):
        return self.books.filter(title__icontains=title)

# Define the Ebook model, inheriting from the Book model
class Ebook(Book):
    file_format = models.CharField(max_length=20)

    # Overriding the display_info method to include file format attribute
    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, File Format: {self.file_format}"

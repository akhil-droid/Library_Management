from django.urls import path
from .views import (
    AddBookView,
    ListBooksView,
    DeleteBookView,
    UpdateBookView,
    AddLibraryView,
    AddBookToLibraryView,
    DisplayAllBooksInLibraryView,
    SearchBookByTitleView,
    AddEbookView,
    ListEbooksView,
    DeleteEbookView,
    UpdateEbookView


)
# Defining URL patterns for the library system
urlpatterns = [

    # URL pattern to add, display, delete, update the books.
    path('add-book/', AddBookView.as_view(), name='add_book'),
    path('list-books/', ListBooksView.as_view(), name='list_books'),
    path('delete-book/', DeleteBookView.as_view(), name='delete_book'),
    path('update-book/', UpdateBookView.as_view(), name='update_book'),

    # URL pattern to add, display, delete, update the books in the Library.
    path('add-library/', AddLibraryView.as_view(), name='add_library'),
    path('add-book-to-library/', AddBookToLibraryView.as_view(), name='add_book_to_library'),
    path('<int:library_id>/display-books/', DisplayAllBooksInLibraryView.as_view(), name='display_books_in_library'),
    path('<int:library_id>/search-book/<str:title>/', SearchBookByTitleView.as_view(), name='search_book_by_title'),
    
    # URL pattern to add, display, delete, update the ebooks.
    path('add-ebook/', AddEbookView.as_view(), name='add_ebook'),
    path('list-ebooks/', ListEbooksView.as_view(), name='list_ebooks'),
    path('delete-ebook/', DeleteEbookView.as_view(), name='delete_ebook'),
    path('update-ebook/', UpdateEbookView.as_view(), name='update_book'),
]

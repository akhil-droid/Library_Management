from django.http import JsonResponse, HttpResponseBadRequest
from django.views import View
from .models import Book, Library, Ebook
import json


# View to add a new book
class AddBookView(View):
    # Method to perform POST operation on the books
    def post(self, request):
        data = json.loads(request.body)
        try:
            # Creating a new Book object with the provided data from the request body
            book = Book.objects.create(
                title=data['title'],
                author=data['author'],
                isbn=data['isbn']
            )
            # Return a success message with the book title
            return JsonResponse({'message': 'Book added', 'book': book.title})
        except KeyError:
            # Return an error response if required fields are missing
            return HttpResponseBadRequest('Missing required fields')

# View to list all books
class ListBooksView(View):
    def get(self, request):
        # Retrieve all books and convert them to a list
        books = list(Book.objects.all().values())
        return JsonResponse(books, safe=False)

# View to delete a book
class DeleteBookView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            # Find the book using the provided ISBN
            book = Book.objects.get(isbn=data['isbn'])
            # Delete the book
            book.delete()
            return JsonResponse({'message': 'Book deleted'})
        except Book.DoesNotExist:
            return HttpResponseBadRequest('Book not found')
        
# View to update a book's information
class UpdateBookView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            # Find the book using the provided ISBN
            book = Book.objects.get(isbn=data['isbn'])
            # Update fields based on provided data
            book.title = data.get('title', book.title)
            book.author = data.get('author', book.author)
            # Save the updated book instance
            book.save()
            return JsonResponse({'message': 'Book updated successfully', 'book': book.display_info()})
        except Book.DoesNotExist:
            return HttpResponseBadRequest('Book not found')
        except KeyError:
            return HttpResponseBadRequest('Missing required fields')
        except Exception as e:
            return HttpResponseBadRequest(str(e))


# View to add a new library
class AddLibraryView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            # Create a new Library object
            library = Library.objects.create()
            return JsonResponse({'message': 'Library created', 'library_id': library.id})
        except KeyError:
            return HttpResponseBadRequest('Error creating library')

# View to add a book to a library
class AddBookToLibraryView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            # Find the library using the provided ID
            library = Library.objects.get(id=data['library_id'])
            # Find the book using the provided ISBN
            book = Book.objects.get(isbn=data['isbn'])
            # Adding the book to the library
            library.add_book(book)
            return JsonResponse({'message': 'Book added to library'})
        except Library.DoesNotExist:
            return HttpResponseBadRequest('Library not found')
        except Book.DoesNotExist:
            return HttpResponseBadRequest('Book not found')
        
# View to display all books in a library
class DisplayAllBooksInLibraryView(View):
    def get(self, request, library_id):
        try:
            # Find the library using the provided ID
            library = Library.objects.get(id=library_id)
            books_info = library.display_all_books()
            return JsonResponse({'books': books_info})
        except Library.DoesNotExist:
            return HttpResponseBadRequest('Library not found')

# View to search for books by title in a library
class SearchBookByTitleView(View):
    def get(self, request, library_id, title):
        try:
            # Find the library using the provided ID
            library = Library.objects.get(id=library_id)
            # Search for books with titles containing the given title from the request
            books = library.search_by_title(title)
            books_info = [book.display_info() for book in books]
            # Return the books information as a JSON response
            return JsonResponse({'books': books_info})
        except Library.DoesNotExist:
            return HttpResponseBadRequest('Library not found')

# View to add a new ebook
class AddEbookView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            # Create a new Ebook object with the provided data
            ebook = Ebook.objects.create(
                title=data['title'],
                author=data['author'],
                isbn=data['isbn'],
                file_format=data['file_format']
            )
            return JsonResponse({'message': 'EBook added', 'ebook': ebook.title})
        except KeyError:
            return HttpResponseBadRequest('Missing required fields')

# View to list all ebooks
class ListEbooksView(View):
    def get(self, request):
        # Retrieve all ebooks and convert them to a list
        ebooks = list(Ebook.objects.all().values())
        # Return the list of ebooks as a JSON response
        return JsonResponse(ebooks, safe=False)

# View to delete an ebook
class DeleteEbookView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            # Find the ebook using the provided ISBN
            ebook = Ebook.objects.get(isbn=data['isbn'])
            # Deleting the ebook
            ebook.delete()
            return JsonResponse({'message': 'EBook deleted'})
        except Ebook.DoesNotExist:
            return HttpResponseBadRequest('EBook not found')
        
# View to update an ebook's information
class UpdateEbookView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            # Fetch the ebook using ISBN
            ebook = Ebook.objects.get(isbn=data['isbn'])
            # Update fields based on provided data
            ebook.title = data.get('title', ebook.title)
            ebook.author = data.get('author', ebook.author)
            ebook.file_format = data.get('field_format', ebook.file_format)
            # Save the updated book instance
            ebook.save()
            return JsonResponse({'message': 'Ebook updated successfully', 'ebook': ebook.display_info()})
        except Ebook.DoesNotExist:
            return HttpResponseBadRequest('Ebook not found')
        except KeyError:
            return HttpResponseBadRequest('Missing required fields')
        except Exception as e:
            return HttpResponseBadRequest(str(e))


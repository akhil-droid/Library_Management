# Library_Management
A Django project which implements the library system where you can add , update, delete and display the books, libraries and ebooks

## URLs to Test the functionality and perform the CRUD operations of the Library APP in POstman.
#### 1) URL for adding a new book
   ##### POST method - http://127.0.0.1:8000/library/add-book/
   ##### sample body -
   {
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "isbn": "9780743273565"
   }

#### 2) URL for displaying the books
   ##### GET method - http://127.0.0.1:8000/library/list-books/

#### 3) URL for deleting a book
   ##### POST method - http://127.0.0.1:8000/library/delete-book/
   ##### sample body -
   {
  "isbn": "9780743273565"
   }

#### 4) URL for updating a new book
   ##### POST method - http://127.0.0.1:8000/library/update-book/
   ##### sample body -
   {
  "title": "The Great Gatsby",
  "author": "Akhil",
  "isbn": "9780743273565"
   }

#### 5) URL for adding a new library
   ##### POST method - http://127.0.0.1:8000/library/add-library/
   ##### sample body -
   {}

#### 6) URL for adding a book to the library
   ##### POST method - http://127.0.0.1:8000/library/add-book-to-library/
   ##### sample body -
   {
  "library_id": 1,
  "isbn": "9780743273565"
   }

#### 7) URL for displaying the books of a library
   ##### POST method - http://127.0.0.1:8000/library/<int:library_id>/display-books/

#### 8) URL for searching a book of a library
   ##### POST method - http://127.0.0.1:8000/library/<int:library_id>/search-book/<str:title>/

#### 9) URL for adding a new ebook
   ##### POST method - http://127.0.0.1:8000/library/add-ebook/
   ##### sample body -
   {
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "isbn": "9780713273565"
  "file_format": "PDF"
   }

#### 10) URL for displaying the ebooks
   ##### GET method - http://127.0.0.1:8000/library/list-ebooks/

#### 11) URL for deleting a ebook
   ##### POST method - http://127.0.0.1:8000/library/delete-ebook/
   ##### sample body -
   {
  "isbn": "9780713273565"
   }

#### 12) URL for updating a new ebook
   ##### POST method - http://127.0.0.1:8000/library/update-ebook/
   ##### sample body -
   {
  "title": "The Great Gatsby",
  "author": "Akhil",
  "isbn": "9780743273505"
  "file_format": "PDF"
   }

   

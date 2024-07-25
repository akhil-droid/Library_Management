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

2) URL for displaying the books
   GET method - http://127.0.0.1:8000/library/list-books/

3) URL for deleting a book
   POST method - http://127.0.0.1:8000/library/delete-book/
   sample body -
   {
  "isbn": "9780743273565"
   }

4) URL for updating a new book
   POST method - http://127.0.0.1:8000/library/update-book/
   sample body -
   {
  "title": "The Great Gatsby",
  "author": "Akhil",
  "isbn": "9780743273565"
   }
   

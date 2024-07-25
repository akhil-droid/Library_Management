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
   <img width="960" alt="image" src="https://github.com/user-attachments/assets/80bac837-c5c0-4faa-aa81-24c40de5714e">

#### 2) URL for displaying the books
   ##### GET method - http://127.0.0.1:8000/library/list-books/
   <img width="960" alt="image" src="https://github.com/user-attachments/assets/51450ba8-1beb-481e-83c7-3b695d3ff025">

#### 3) URL for updating a new book
   ##### POST method - http://127.0.0.1:8000/library/update-book/
   ##### sample body -
   {
  "title": "The Great Gatsby",
  "author": "Akhil",
  "isbn": "9780743273565"
   }
   ![image](https://github.com/user-attachments/assets/0bc2c0c1-c505-4c69-889b-cfe3be8f409e)

#### 4) URL for deleting a book
   ##### POST method - http://127.0.0.1:8000/library/delete-book/
   ##### sample body -
   {
  "isbn": "9780743273565"
   }
   ![image](https://github.com/user-attachments/assets/00a26eff-2aa0-4174-861e-50b42415fb14)

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

   

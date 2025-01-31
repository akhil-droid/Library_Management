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
   ![image](https://github.com/user-attachments/assets/1fc45624-32ca-4366-8145-543c0bc9aa54)

#### 6) URL for adding a book to the library
   ##### POST method - http://127.0.0.1:8000/library/add-book-to-library/
   ##### sample body -
   {
  "library_id": 1,
  "isbn": "9780743273565"
   }
   ![image](https://github.com/user-attachments/assets/31ec7520-5ac9-46c1-b442-e4fa1c94fae2)

#### 7) URL for displaying the books of a library
   ##### POST method - http://127.0.0.1:8000/library/<int:library_id>/display-books/
   ![image](https://github.com/user-attachments/assets/0bd31030-6c13-4f3a-97f1-bc970fa06a29)

#### 8) URL for searching a book of a library
   ##### POST method - http://127.0.0.1:8000/library/<int:library_id>/search-book/<str:title>/
   ![image](https://github.com/user-attachments/assets/601caabe-3c5f-4af8-afaf-fb80869ffbf3)

#### 9) URL for adding a new ebook
   ##### POST method - http://127.0.0.1:8000/library/add-ebook/
   ##### sample body -
   {
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "isbn": "9780713273565",
  "file_format": "PDF"
   }
   ![image](https://github.com/user-attachments/assets/3294cc45-4db8-45e8-940c-25f5351333f5)

#### 10) URL for displaying the ebooks
   ##### GET method - http://127.0.0.1:8000/library/list-ebooks/
   ![image](https://github.com/user-attachments/assets/f24c6411-f203-4c7e-9b8b-9f7a91982fc6)

#### 11) URL for updating a new ebook
   ##### POST method - http://127.0.0.1:8000/library/update-ebook/
   ##### sample body -
   {
  "title": "The Great Gatsby",
  "author": "Akhil",
  "isbn": "9780713273565"
  "file_format": "PDF"
   }
   ![image](https://github.com/user-attachments/assets/d89d3202-ae4c-45c0-b919-d5865b71123a)

#### 12) URL for deleting a ebook
   ##### POST method - http://127.0.0.1:8000/library/delete-ebook/
   ##### sample body -
   {
  "isbn": "9780713273565"
   }
   ![image](https://github.com/user-attachments/assets/55473d1d-3390-4608-ad76-585dbfbeedf1)

   

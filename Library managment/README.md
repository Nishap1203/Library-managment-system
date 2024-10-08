# Library Management System

## Features

- **Add Books:** Add new books to the library with a unique identifier, title, author, and publication year.
- **Borrow Books:** Borrow a book from the library, provided it is available.
- **Return Books:** Return a borrowed book, updating its availability.
- **View Available Books:** View a list of all books currently available in the library.

## Project Structure

- `src/`
  - `library.py`: Contains the implementation of the Library Management System.
- `tests/`
  - `test_library.py`: Contains test cases for the library functionality.
- `README.md`: This file.

## Setup and Installation

1. **Clone the Repository:**
   ```sh
   git clone <remote-repository-url>
   cd library_management_system
2.**Create and Activate Virtual Environment:**
```sh
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
3.**Install Dependencies:**
```sh
pip install pytest

git remote add origin <remote-repository-url>
git push -u origin master

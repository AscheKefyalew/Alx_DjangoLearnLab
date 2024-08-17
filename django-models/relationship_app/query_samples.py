import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project_name.settings")  # Replace with your project name
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = author.books.all()
        for book in books:
            print(f"Book: {book.title}")
    except Author.DoesNotExist:
        print("Author not found")

def list_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        for book in books:
            print(f"Book: {book.title}")
    except Library.DoesNotExist:
        print("Library not found")

def retrieve_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian
        print(f"Librarian: {librarian.name}")
    except Library.DoesNotExist:
        print("Library not found")
    except Librarian.DoesNotExist:
        print("Librarian not found")

if __name__ == "__main__":
    # Replace with actual values for testing
    query_books_by_author("Author Name")
    list_books_in_library("Library Name")
    retrieve_librarian_for_library("Library Name")

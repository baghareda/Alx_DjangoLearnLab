from relationship_app.models import Author, Book, Librarian

# Create authors
orwell = Author.objects.create(name="George Orwell")
huxley = Author.objects.create(name="Aldous Huxley")

# Create books
book1 = Book.objects.create(title="1984")
book2 = Book.objects.create(title="Brave New World")

# Link authors to books
book1.authors.add(orwell)
book2.authors.add(huxley)

# Create librarian
librarian = Librarian.objects.create(name="Sofia", library="Central Library")

# Query all books
print("All books:", Book.objects.all())

# Query authors of a book
print("Authors of 1984:", book1.authors.all())

# Query books by an author
print("Books by George Orwell:", orwell.book_set.all())

# Get librarian info
print("Librarians:", Librarian.objects.all())

def list_books_in_library(library_name):
    from relationship_app.models import Library

    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        for book in books:
            print(book.title)
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")

def list_librarians_in_library(library_name):
    from relationship_app.models import Library

    try:
        library = Library.objects.get(name=library_name)
        librarians = library.librarians.all()
        for librarian in librarians:
            print(librarian.name)
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")

def list_libraries_by_author(author_name):
    from relationship_app.models import Author

    try:
        author = Author.objects.get(name=author_name)
        books = author.books.all()
        libraries = set()

        for book in books:
            libraries.add(book.library.name)

        for library in libraries:
            print(library)

    except Author.DoesNotExist:
        print(f"Author '{author_name}' not found.")


def list_books_in_library(library_name):
    from relationship_app.models import Library

    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        for book in books:
            print(f"{book.title} by {book.author.name}")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")


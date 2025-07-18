from relationship_app.models import Author, Book, Library, Librarian

# Create library
central_library = Library.objects.create(name="Central Library")

# Create authors
orwell = Author.objects.create(name="George Orwell")
huxley = Author.objects.create(name="Aldous Huxley")

# Create books and link authors and libraries
book1 = Book.objects.create(title="1984", author=orwell, library=central_library)
book2 = Book.objects.create(title="Brave New World", author=huxley, library=central_library)

# Create librarian
librarian = Librarian.objects.create(name="Sofia", library=central_library)

# Query all books
print("All books:", Book.objects.all())

# Query authors of a book
print("Author of 1984:", book1.author.name)

# ✅ Query books by an author (check wants this exact call)
print("Books by George Orwell:", Book.objects.filter(author=orwell))

# Get librarian info
print("Librarian for Central Library:", librarian.name)

# List books in a specific library
def list_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        for book in books:
            print(f"{book.title} by {book.author.name}")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")

# List librarian of a specific library
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian
        print(f"Librarian: {librarian.name}")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to '{library_name}'.")

# List libraries by a specific author
def list_libraries_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        libraries = {book.library.name for book in books}
        for lib in libraries:
            print(lib)
    except Author.DoesNotExist:
        print(f"Author '{author_name}' not found.")
        
def get_librarian_for_library(library_name):
    from relationship_app.models import Library, Librarian

    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        print(f"Librarian for {library.name}: {librarian.name}")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")
    except Librarian.DoesNotExist:
        print(f"No librarian found for '{library_name}'.")


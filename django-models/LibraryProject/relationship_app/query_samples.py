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

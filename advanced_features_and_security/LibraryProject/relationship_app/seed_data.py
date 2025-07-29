from relationship_app.models import Library, Author, Book, Librarian

def run():
    # Clear old data
    Library.objects.all().delete()
    Author.objects.all().delete()
    Book.objects.all().delete()
    Librarian.objects.all().delete()

    # Create Library
    lib = Library.objects.create(name="Central Library")

    # Create Authors
    author1 = Author.objects.create(name="George Orwell")
    author2 = Author.objects.create(name="Aldous Huxley")

    # Create Books
    Book.objects.create(title="1984", author=author1, library=lib)
    Book.objects.create(title="Brave New World", author=author2, library=lib)

    # Create Librarian
    Librarian.objects.create(name="John Doe", library=lib)

    print("✅ Seed data created successfully")

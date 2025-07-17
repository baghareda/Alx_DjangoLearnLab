# CRUD Operations – Full Flow

## Create

```python
from bookshelf.models import Book
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()
print(book.id)

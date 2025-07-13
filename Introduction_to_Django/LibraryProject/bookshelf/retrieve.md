# Retrieve Operation

```python
from bookshelf.models import Book
book = Book.objects.filter(title="1984").first()
print(book.title)
print(book.author)
print(book.publication_year)

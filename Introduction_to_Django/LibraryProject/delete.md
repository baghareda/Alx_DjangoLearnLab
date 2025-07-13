# Delete Operation

```python
from bookshelf.models import Book
book = Book.objects.filter(title="Nineteen Eighty-Four").first()
book.delete()
Book.objects.all()

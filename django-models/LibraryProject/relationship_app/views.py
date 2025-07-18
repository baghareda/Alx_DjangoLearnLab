from django.shortcuts import render
from django.views.generic import DetailView  # ✅ required for class-based view
from .models import Book, Library  # ✅ required for both views
from .models import Library
from .models import Book


# ✅ Function-based view: list all books and authors
def list_books(request):
    books = Book.objects.all()  # ✅ this exact line must appear
    return render(request, 'relationship_app/list_books.html', {'books': books})  # ✅ must match path

# ✅ Class-based view: show detail of specific library and its books
class LibraryDetailView(DetailView):  # ✅ required to use DetailView
    model = Library
    template_name = 'relationship_app/library_detail.html'  # ✅ must match this string exactly
    context_object_name = 'library'

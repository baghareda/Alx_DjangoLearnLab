from django.shortcuts import render
from django.views.generic import DetailView  # ✅ This line is critical
from .models import Book, Library

def list_books(request):
    books = Book.objects.select_related('author').all()
    return render(request, 'list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'

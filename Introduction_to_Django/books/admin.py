from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')  # Columns in list view
    search_fields = ('title', 'author')  # Enables search bar

admin.site.register(Book, BookAdmin)

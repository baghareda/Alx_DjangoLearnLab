from django.contrib import admin
from .models import Library, Author, Book, Librarian, UserProfile

@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'library']
    list_filter = ['library', 'author']
    search_fields = ['title', 'author__name']

@admin.register(Librarian)
class LibrarianAdmin(admin.ModelAdmin):
    list_display = ['name', 'library']

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'role']
    list_filter = ['role']

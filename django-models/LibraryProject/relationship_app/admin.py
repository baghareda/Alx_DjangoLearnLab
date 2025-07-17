from django.contrib import admin
from .models import Author, Profile, Book, Reader

admin.site.register(Author)
admin.site.register(Profile)
admin.site.register(Book)
admin.site.register(Reader)

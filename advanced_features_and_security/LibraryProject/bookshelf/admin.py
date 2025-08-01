from django.contrib import admin
from .models import Book
from django.contrib import admin
from .models import CustomUser


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('publication_year',)
    search_fields = ('title', 'author')
    
class CustomUserAdmin(admin.ModelAdmin):
    pass  # minimal stub admin

admin.site.register(CustomUser, CustomUserAdmin)

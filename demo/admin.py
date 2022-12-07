from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Book
# Register your models here.
# admin.site.register(Book)
# this is will register all books, not flexible to change
# the following is a flexible way
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'price']
    list_filter = ['published', 'price']
    search_fields = ['title', 'description']
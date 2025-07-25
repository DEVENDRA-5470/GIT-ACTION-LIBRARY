from django.contrib import admin
from books.models import All_books,Rented_books
# Register your models here.
admin.site.register(All_books)
admin.site.register(Rented_books)
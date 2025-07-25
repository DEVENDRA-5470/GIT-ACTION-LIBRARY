from django.urls import path
from books.views import *
urlpatterns = [
    path('',create_books,name="create_books"),
    path('all_books/',all_books,name="all_books"),
    path('read_books/<int:id>',read_books,name="read_books"),
    path('update_books/<int:id>',update_books,name="update_books"),
    path('delete_books/<int:id>',delete_books,name="delete_books"),
    path('rented_books/<int:id>',rent_book,name="rented_books"),
]

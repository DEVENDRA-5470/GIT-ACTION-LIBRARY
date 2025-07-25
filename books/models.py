from django.db import models
from author.models import Authors_profile
from django.contrib.auth.models import User
# Create your models here.

class All_books(models.Model):
    author=models.ForeignKey(Authors_profile,on_delete=models.CASCADE,related_name='books')
    book_id=models.CharField(max_length=5,unique=True)
    book_title=models.CharField(max_length=100,blank=True,null=True)
    book_content=models.TextField(blank=True,null=True)
    book_published_at=models.DateTimeField(auto_now_add=True)
    book_updated_at=models.DateTimeField(auto_now=True)
    book_price=models.DecimalField(default=500,max_digits=6,decimal_places=2)
    is_available=models.BooleanField(default=True)

    def __str__(self):
        return f'{self.book_title}'

class Rented_books(models.Model):
    book=models.ForeignKey(All_books,on_delete=models.CASCADE,related_name="rented_books")
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="rented_books")
    rented_at=models.DateTimeField(auto_now_add=True)
    return_at=models.DateField()
    amount_paid=models.DecimalField(max_digits=6,decimal_places=2)

    def __str__(self):
        return f'{self.book.book_title}'
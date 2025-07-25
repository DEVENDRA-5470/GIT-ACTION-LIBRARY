from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Authors_profile(models.Model):
    author=models.OneToOneField(User,on_delete=models.CASCADE)
    author_img=models.ImageField(upload_to='author_uploads/')
    author_name=models.CharField(max_length=200)
    author_mob=models.CharField(max_length=12,blank=True,null=True,unique=True)
    author_email=models.CharField(max_length=200,blank=True,null=True,unique=True)
    author_education=models.CharField(max_length=100,blank=True,null=True)
    author_books=models.TextField(blank=True,null=True)
    author_about=models.TextField(null=True,default="About Me")
    author_created_at=models.DateTimeField(auto_now=True)
    author_update_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username}"
        

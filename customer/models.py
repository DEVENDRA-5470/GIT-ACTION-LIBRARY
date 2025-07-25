from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class students_profile(models.Model):
    student=models.OneToOneField(User,on_delete=models.CASCADE)
    student_img=models.ImageField(upload_to='student_uploads/')
    student_name=models.CharField(max_length=200)
    student_mob=models.CharField(max_length=12,blank=True,null=True,unique=True)
    student_email=models.CharField(max_length=200,blank=True,null=True,unique=True)
    student_education=models.CharField(max_length=100,blank=True,null=True)
    student_about=models.TextField(null=True,default="About Me")
    student_rented_books=models.TextField(blank=True,null=True)
    student_created_at=models.DateTimeField(auto_now=True)
    student_update_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username}"
        

from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from customer.models import students_profile;

@receiver(post_save,sender=User)
def create_student_profile(sender,instance,created,**kwargs):
    if created:
        students_profile.objects.create(student=instance)

        
def save_student_profile(sender,instance,created,**kwargs):
    if hasattr(instance,'studentprofile'):
        instance.studentprofile.save()

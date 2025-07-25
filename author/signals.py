from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from author.models import Authors_profile;

@receiver(post_save,sender=User)
def create_author_profile(sender,instance,created,**kwargs):
    if created:
        Authors_profile.objects.create(author=instance)
        

def save_author_profile(sender,instance,created,**kwargs):
    if hasattr(instance,'authorprofile'):
        instance.authorprofile.save()
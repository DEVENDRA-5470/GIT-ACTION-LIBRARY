from django.db.models.signals import post_save
from django.dispatch import receiver
from books.models import All_books
from author.models import Authors_profile

@receiver(post_save,sender=All_books)
def update_author_books(sender,instance,created,**kwargs):
    if instance.book_title:
        author_profile=instance.author

        book_titles=list(author_profile.books.values_list('book_title',flat=True))
        author_profile.author_books=','.join(book_titles)
        author_profile.save()
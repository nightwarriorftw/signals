from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.dispatch import Signal
from custom_signal.models import Author
from custom_signal.models import Book


book_published = Signal()

@receiver(pre_delete, sender=Author)
def delete_books(sender, instance, **kwargs):
    return Book.objects.filter(author_id=instance.id).delete()

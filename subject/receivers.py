from django.dispatch import receiver
from subject.signals import book_published
from subject.models import Book

@receiver(book_published, sender=Book)
def book_published_receiver(sender, author, book, **kwargs):
    print('\n\n')
    print(f'{book} published by {author}')
    print('\n\n')

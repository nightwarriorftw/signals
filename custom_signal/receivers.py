from django.dispatch import receiver
from custom_signal.signals import book_published

from custom_signal.tasks import hello_world

@receiver(book_published)
def send_notification_on_book_published(sender, **kwargs):
    author = kwargs.get("author")
    book = kwargs.get("book")
    print(f"{book.title} by {author.name} just got published")

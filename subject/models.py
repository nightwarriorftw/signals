from django.db import models
from django.db import transaction

class Author(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()

    def __str__(self) -> str:
        return f'<{self.name} : {self.email}>'


class Book(models.Model):
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    is_published = models.BooleanField(default=False)
    price = models.FloatField(default=10)
    description = models.TextField()

    def save(self, *args, **kwargs) -> None:
        is_object_created = self.pk
        super().save(*args, **kwargs)
        if is_object_created and self.is_published:
            print(is_object_created, self.is_published)
            from subject.signals import book_published
            with transaction.atomic():
                transaction.on_commit(book_published.send(sender=Book, author=self.author.name, book=self.title))

    def __str__(self) -> str:
        return f'<{self.title} by {self.author.name}>'

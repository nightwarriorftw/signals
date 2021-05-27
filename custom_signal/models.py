from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'<{self.name} : {self.email}>'

class Book(models.Model):
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField()
    is_published = models.BooleanField(default=False)
    price = models.FloatField(default=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def save(self, *args, **kwargs) -> None:
        super().save(*args, **kwargs)
        if self.is_published:
            from custom_signal.signals import book_published
            book_published.send(sender=self.__class__, author=self.author, book=self)

    def __str__(self) -> str:
        return f'<{self.title} by {self.author.name}>'
from django.contrib import admin

from custom_signal.models import Author
from custom_signal.models import Book

admin.site.register(Author)
admin.site.register(Book)

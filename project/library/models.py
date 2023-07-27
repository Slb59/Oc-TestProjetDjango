from django.db import models
# from django.utils import timezone

from ..mixin import DateFields


class Book(DateFields):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.author} | {self.title}'

from django.db import models
# from django.utils import timezone


class DateFields(models.Model):
    """ a common class for timestamping """
    created_time = models.DateTimeField(
        auto_now_add=True
    )
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Book(DateFields):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.author} | {self.title}'

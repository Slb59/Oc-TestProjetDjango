from django.db import models


class DateFields(models.Model):
    """ a common class for timestamping """
    created_time = models.DateTimeField(
        auto_now_add=True
    )
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

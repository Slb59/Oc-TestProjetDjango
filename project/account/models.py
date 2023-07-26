from datetime import datetime, timedelta

from django.db import models
from django.contrib.auth import models as auth_models
from django.db.models import CheckConstraint, Q


class User(auth_models.AbstractUser):
    birth_date = models.DateField(
        blank=False, null=False, default='1970-01-01'
        )
    can_be_contacted = models.BooleanField(default=False)
    can_data_be_shared = models.BooleanField(default=False)

    @property
    def age(self):
        return int((datetime.now().date() - self.birth_date).days / 365.25)

    class Meta:
        constraints = [
            # Ensures constraint on DB level, raises IntegrityError
            CheckConstraint(
                check=Q(birth_date__lte=(
                    datetime.today() - timedelta(days=365*15)
                    )),
                name='check_birth_date',
            ),
        ]

    def get_full_name(self):
        return self.first_name + " " + self.last_name

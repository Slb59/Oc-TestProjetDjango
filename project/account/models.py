from datetime import datetime, timedelta

from django.db import models
from django.contrib.auth import models as auth_models
from django.db.models import CheckConstraint, Q
from django.dispatch import receiver
from django.db.models.signals import post_save

from phonenumber_field.modelfields import PhoneNumberField

from ..mixin import DateFields


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


class Profile(DateFields):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    phone = PhoneNumberField(null=True)
    location = models.CharField(max_length=30, blank=True)
    image = models.ImageField(upload_to='profile_img/', null=True)

    def __str__(self):
        return 'Profile of {}'.format(self.user.get_full_name())


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

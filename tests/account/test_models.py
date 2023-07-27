from project.account.models import User, Profile

import pytest


@pytest.mark.django_db
def test_profile_str():

    """
    Testing whether Profile's __str__ method is implemented properly
    """

    user = User.objects.create(
        username='TestUser',
        password='random_password',
        birth_date='1970-01-01'
        )
    profile = Profile(user=user)

    assert str(profile) == f"Profile of {user.get_full_name()}"

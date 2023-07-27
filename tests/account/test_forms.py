
from project.account.models import User
from project.account.forms import SignUpForm

import pytest


@pytest.mark.django_db
def test_signup_form_validate():

    """
    Testing the SignUpForm to check if the user input
    data is properly validated or not
    """

    temp_user = {
        'username': 'TestUser',
        'password': 'test-password',
        'email': 'testuser@testing.com',
        'first_name': 'Test',
        'last_name': 'User',
        'birth_date': '1970-01-01'
    }

    user = SignUpForm(data=temp_user)

    assert user.is_valid()


@pytest.mark.django_db
def test_signup_form_save_method():

    """
    Testing if the User object is created properly by using SignUpForm or not
    """

    temp_user = {
        'username': 'TestUser',
        'password': 'test-password',
        'email': 'testuser@testing.com',
        'first_name': 'Test',
        'last_name': 'User',
        'birth_date': '1970-01-01'
    }

    form = SignUpForm(data=temp_user)
    user = form.save()

    assert isinstance(user, User)

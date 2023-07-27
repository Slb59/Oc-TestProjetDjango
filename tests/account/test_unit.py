# from datetime import datetime 
from django.test import TestCase
from django.db.utils import IntegrityError


from project.account.models import User, Profile


class UserTestCase(TestCase):
    """ tests the model User """

    @classmethod
    def setUpTestData(cls) -> None:
        # Create a user
        testuser1 = User.objects.create_user(
            username='testuser1', password='98765abc',
            email='testuser1@gmail.com',
            birth_date='1970-01-01'
            )
        testuser1.save()
        return super().setUpTestData()

    def test_user_content(self):
        user = User.objects.get(username='testuser1')
        email = f'{user.email}'
        self.assertEqual(email, 'testuser1@gmail.com')

    def test_user_minus15years(self):
        with self.assertRaises(Exception) as raised:
            User.objects.create_user(
                username='testuser2', password='98765abc',
                email='testuser2@gmail.com',
                birth_date='2023-01-01'
            )
        self.assertEqual(IntegrityError, type(raised.exception))

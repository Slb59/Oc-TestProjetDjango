import pytest

from django.test import Client
from library.models import Book


@pytest.mark.django_db
def test_book_model():
    Client()
    book = Book.objects.create(
               author="Jules Verne",
               title="20 milles lieues sous les mers")
    expected_value = "Jules Verne | 20 milles lieues sous les mers"
    assert str(book) == expected_value

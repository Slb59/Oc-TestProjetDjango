import pytest

from django.urls import reverse, resolve
from project.library.models import Book


@pytest.mark.django_db
def test_book_infos_url():
    Book.objects.create(author="Jules Verne",
                        title="20 milles lieues sous les mers")
    path = reverse('infos', kwargs={'pk': 1})

    assert path == "/1"
    assert resolve(path).view_name == "infos"

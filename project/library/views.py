from django.shortcuts import get_object_or_404, render
from .models import Book


def book_infos(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, "book_infos.html", {'book': book})

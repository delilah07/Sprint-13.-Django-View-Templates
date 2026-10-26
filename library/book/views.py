from django.shortcuts import render
from .models import Book


def book_list(request):
    book = Book.get_all()
    return render(request, 'book/book_list.html', {
        'book': book
    })
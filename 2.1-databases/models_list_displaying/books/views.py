from django.shortcuts import render
from .models import Book
from datetime import datetime as dt
from django.core.paginator import Paginator


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, template, context)


def books_by_date(request, pub_date):
    template = 'books/books_by_date.html'
    pub_date = dt.strptime(pub_date, "%Y-%m-%d").date()
    books = Book.objects.filter(pub_date=pub_date)
    context = {
        'books': books,
    }
    return render(request, template, context)

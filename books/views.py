from django.shortcuts import render, redirect
from books.models import Book
from django.core.paginator import Paginator
from datetime import datetime
import datetime

def index(request):
    return redirect('books')

def books_view(request):
    template = 'books/books_list.html'
    _books_list = Book.objects.all()
    context = {"books": _books_list}
    return render(request, template, context)


def date_book(request, select_date):
    template = 'books/book_for_date.html'
    _books_list = Book.objects.filter(pub_date=select_date)
    prev = None
    next = None
    all = Book.objects.all().order_by('pub_date').distinct('pub_date')
    for p in range(len(all)):
        if all[p].pub_date != select_date.date():
            prev = all[p].pub_date
        else:
            if p != len(all)-1:
                next = all[p+1].pub_date
                break
    print(prev)
    print(next)

    context = {"books": _books_list,
               "prev_date": prev,
               "next_date": next,
               }
    return render(request, template, context)


# def date_book(request, selected_date):
#     template = 'books/book_for_date.html'
#     _book_today = Book.objects.filter(pub_date=selected_date)
#     ord_dates = Book.objects.all().order_by('pub_date')
#     list_dates = [i.pub_date.strftime('%Y-%m-%d') for i in ord_dates]
#     date_index = list_dates.index(selected_date.strftime('%Y-%m-%d'))
#     prev_date = list_dates[int(date_index)-1]
#     next_date = list_dates[int(date_index)+1]
#     print(prev_date)
#     print(next_date)
#     context = {"books": _book_today,
#                "p_d": prev_date,
#                "n_d": next_date}
#     return render(request, template, context)
from django.shortcuts import render, redirect
from books.models import Book


def index(request):
    return redirect('books')


def books_view(request):
    template = 'books/books_list.html'
    books_list = Book.objects.all()
    context = {"books": books_list}
    return render(request, template, context)


# Создаем пагинацию по датам, для чего необходимо отсортировать книги в БД по датам
# и определить предыдущую и последующую даты
def date_book(request, select_date):
    template = 'books/book_for_date.html'
    books_list = Book.objects.filter(pub_date=select_date)
    prev_date = None  # предыдущая дата. None - на случай если её нет
    next_date = None  # следующая дата. None - на случай если её нет
    # Сортируем БД по датам. distintc - только уникальные значения
    ordered_books = Book.objects.all().order_by('pub_date').distinct('pub_date')

    # Проходим по всем датам. если дата БД не соответствует выбранной на странице,
    # присваем prev_date значение даты. И так пока не дойдем до выбранной. После
    # проверяем что дата не последняя в списке. И присваем next_date значение следующей даты
    for i in range(len(ordered_books)):
        if ordered_books[i].pub_date != select_date.date():
            prev_date = ordered_books[i].pub_date
        else:
            if i != len(ordered_books)-1:
                next_date = ordered_books[i+1].pub_date
                break

    context = {"books": books_list,
               "prev_date": prev_date,
               "next_date": next_date,
               }
    return render(request, template, context)


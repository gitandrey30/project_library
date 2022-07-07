from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView
from django.views.generic.detail import SingleObjectMixin

from .forms import NewBookForm, NewAccountForm
from .models import Book, Reader


def main_page(request):
    return render(request)


def add_new_book(request):
    form = NewBookForm()
    context = {'form': form}
    if request.method == 'POST':
        form = NewBookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return render(request, 'add_new_book.html', context)


def add_new_account(request):
    account_form = NewAccountForm()
    context = {'form': account_form}
    if request.method == 'POST':
        account_form = NewAccountForm(request.POST)
    return render(request, 'new_account_page.html', context)


def get_home_page(request):
    return render(request, 'home_page.html', {'title': 'домашняя страница'})


def request_new_book(request):
    return render(request, 'find_new_book.html')


def show_book_list(request):
    book_list = Book.objects.all()
    context = {'book_list': book_list}
    print(book_list)
    return render(request, 'book_list.html', context)

# class BookListView(ListView):
#     model = Book
#     template_name = 'book_list.html'
#     paginate_by = 1
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         print(context)
#         context['title'] = 'title'
#         return context

def show_readers(request):
    readers = Reader.objects.all()
    context = {'readers': readers}
    print(readers)
    return render(request, 'reader_list.html', context)


class ReaderListView(ListView):
    model = Reader
    template_name = 'reader_list.html'
    #extra_context = {'title': 'список читателей'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'список читателей'
        context['cat_selected'] = 0
        return context

    # def get_queryset(self):
    #     return Reader.objects.filter(amount >= 1)


def about_storage(request):
    return render(request, 'main_page.html', {'title': 'домашняя страница'})


def contact(request):
    return HttpResponse(request, 'обратная связь')


def get_error(request):
    return render(request, 'error.html')
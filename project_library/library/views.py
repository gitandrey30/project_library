from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import NewBookForm, NewAccountForm
from .models import Book, Reader
from django.views.generic import ListView


def main_page(request):
    return render(request)


def add_new_book(request):
    if request.method == 'POST':
        form = NewBookForm()
        context = {'form': form}
        return render(request, 'add_new_book.html', context)


def add_new_account(request):
    if request.method == 'POST':
        account_form = NewAccountForm(request.POST, request.FILES)
        if account_form.is_valid():
            account_form.save()
            return render(request, 'new_account_page')
        else:
            account_form = NewAccountForm()
            context = {'form': account_form}
            return render(request, 'error.html', context)
    return render(request, 'new_account_page.html')


def get_home_page(request):
    return render(request, 'home_page.html', {'title': 'домашняя страница'})


def request_new_book(request):
    return render(request, 'find_new_book.html')


class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    paginate_by = 1
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context['title'] = 'title'
        return context
        #сематика

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
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import ListView
from django.views.generic.detail import SingleObjectMixin

from .forms import NewBookForm, NewAccountForm
from .models import Book, Reader


# def main_page(request):
#     return render(request)


def add_new_book(request):
    form = NewBookForm()
    context = {'form': form,
               'title': 'добавление новой книги'
               }
    if request.method == 'POST':
        form = NewBookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return render(request, 'add_new_book.html', context)


def add_new_account(request):
    account_form = NewAccountForm()
    context = {'form': account_form,
               'title': 'добавление нового аккаунта'
               }
    if request.method == 'POST':
        account_form = NewAccountForm(request.POST)
        if account_form.is_valid():
            account_form.save()
    return render(request, 'new_account_page.html', context)


def get_home_page(request):
    return render(request, 'home_page.html', {'title': 'домашняя страница'})


def request_new_book(request):
    return render(request, 'find_new_book.html', {'title': 'запрос новой книги'})


class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'

    # paginate_by = 1
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context['title'] = 'страница доступных книг'
        return context


class ReaderListView(ListView):
    model = Reader
    template_name = 'reader_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context['title'] = 'список читателей'
        return context

    # def get_queryset(self):
    #     return Reader.objects.filter(amount >= 1)


def about_storage(request):
    return render(request, 'main_page.html', {'title': 'домашняя страница'})


def contact(request):
    return HttpResponse(request, 'обратная связь')


def get_error(request):
    return render(request, 'error.html')


# def authentication(request):
#     auth_form = AuthForm(data=request.POST)
#     context = {'auth_form': auth_form,
#                'title': 'аутентификация'
#                }
#     if request.method == 'POST':
#         if auth_form.is_valid():
#             # user = verify_form.get_user()
#             # # login(request, user)
#             return redirect
#     else:
#         auth_form = AuthForm()
#     return render(request, 'login.html', context)

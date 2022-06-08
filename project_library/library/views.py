from django.shortcuts import render

from .forms import NewBookForm, NewAccountForm
from .models import Book


def add_new_book(request):
    form = NewBookForm()
    context = {'form': form}
    if request.method=='POST':
        form=NewBookForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'add_new_book.html', context)


def add_new_account(request):
    account_form=NewAccountForm()
    context = {'form':account_form}
    # if account_form.is_valid():
    #     account_form.save()
    return render(request,'new_account_page.html',context)
from django.urls import path

from .views import get_home_page, add_new_book, add_new_account, request_new_book, BookListView, get_error, \
    ReaderListView

# app_name = 'library'

urlpatterns = [
    path('', get_home_page, name='main'),
    path('add_new_book/', add_new_book, name='add_new_book'),
    path('new_acc/', add_new_account, name='new_acc'),
    path('find_new_book/', request_new_book, name='find_new_book'),
    path('book_list/', BookListView.as_view(), name='book_list'),
    path('reader_list/', ReaderListView.as_view(), name='reader_list'),
    path('error.html/', get_error, name='error'),
    # path('login/', authentication, name='authentication'),
    ]
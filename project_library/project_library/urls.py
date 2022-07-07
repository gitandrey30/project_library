"""project_library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from library.views import add_new_book, add_new_account, get_home_page, request_new_book, BookListView, main_page, ReaderListView, get_error


app_name = 'library'
urlpatterns = [
    path('', get_home_page, name='main'),
    path('admin/', admin.site.urls),
    path('add_new_book/', add_new_book, name='add_new_book'),
    path('new_acc/', add_new_account, name='new_acc'),
    path('find_new_book/', request_new_book, name='find_new_book'),
    path('book_list/', BookListView.as_view(), name='book_list'),
    path('main_page/', main_page, name='main_page'),
    path('reader_list/', ReaderListView.as_view(), name='reader_list'),
    path('error.html/', get_error, name='error')
]

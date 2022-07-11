from django import forms

from .models import Book, Reader


class NewBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"

class NewAccountForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Reader
        fields = "__all__"

# class AuthForm(forms.Form):
#     login = forms.CharField(widget=forms.TextInput, label='введите login')
#     password = forms.CharField(widget=forms.PasswordInput, label='введите пароль')
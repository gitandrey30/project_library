from django import forms

from .models import Book


class New_book_form(forms.ModelForm):
    class Meta:
        model=Book
        fields=[*]

class New_account_form(forms.Form):
    first_name=forms.CharField(label='first_name',max_length=15)
    last_name=forms.CharField(label='last_name',max_length=15)
    email=forms.EmailField(label='email')
    password=forms.PasswordInput(render_value=True)

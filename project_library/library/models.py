from django.db import models


class Book(models.Model):
    book_name_rus=models.CharField(max_length=30)
    book_name_eng=models.CharField(max_length=30)
    genre=models.CharField(max_length=30)
    price=models.DecimalField(max_digits=7, decimal_places=2)
    amount=models.IntegerField()
    all_authors=models.CharField(max_length=50)
    image_front=models.ImageField(upload_to='media')
    image_authors=models.ImageField(upload_to='media')
    price_to_one_day=models.IntegerField()
    year_publication=models.IntegerField()
    date_of_registration=models.IntegerField()
    amount_pages=models.IntegerField()

class Reader(models.Model):
    surname=models.CharField(max_length=10)
    name=models.CharField(max_length=10)
    patronymic=models.CharField(max_length=15)
    number_passport=models.CharField(max_length=10, blank=True, null=True)
    date_of_birth=models.CharField(max_length=10)
    email=models.EmailField()
    address=models.CharField(max_length=30)





from django.db import models


class Book(models.Model):
    CHOICE_GENRE = [
        ('T', 'Technical'),
        ('P', 'Python education'),
        ('M', 'Manual for medical equipment')
                ]
    book_name_rus = models.CharField(max_length=30, verbose_name='название на русском')
    book_name_eng = models.CharField(max_length=30, verbose_name='название на английском')
    genre = models.CharField(max_length=30, verbose_name='жанр', choices=CHOICE_GENRE)
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='цена')
    amount = models.IntegerField(blank=True, verbose_name='колличество')
    all_authors = models.CharField(max_length=50, verbose_name='все авторы данного материала')
    image_front = models.ImageField(upload_to='media', verbose_name='фоторграфия обложки')
    image_authors = models.ImageField(upload_to='media', verbose_name='фотография авторов')
    price_to_one_day = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена аренды за 1 день')
    year_publication = models.DateField(help_text='введите год публикации', verbose_name='год издания')
    date_of_registration = models.DateField(verbose_name='дата регистрации ')
    amount_pages = models.IntegerField(blank=True, verbose_name='колличество страниц')
    file = models.FileField(upload_to='files', verbose_name='выберете файл для загрузки')

    def __str__(self):
        return self.book_name_eng


class Reader(models.Model):
    surname = models.CharField(max_length=10)
    name = models.CharField(max_length=10)
    patronymic = models.CharField(max_length=15)
    number_passport = models.CharField(max_length=10, blank=True, null=True)
    date_of_birth = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.CharField(max_length=30)

    def __str__(self):
        return self.surname




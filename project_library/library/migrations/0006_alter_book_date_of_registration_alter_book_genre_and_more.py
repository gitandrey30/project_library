# Generated by Django 4.0.5 on 2022-06-28 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_alter_book_date_of_registration_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date_of_registration',
            field=models.DateField(auto_now_add=True, verbose_name='дата регистрации '),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('T', 'Technical'), ('P', 'Python education'), ('M', 'Manual for medical equipment')], max_length=30, verbose_name='жанр'),
        ),
        migrations.AlterField(
            model_name='book',
            name='year_publication',
            field=models.DateField(help_text='введите реальный год публикации', verbose_name='год издания'),
        ),
    ]

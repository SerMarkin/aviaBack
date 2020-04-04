# Generated by Django 3.0.4 on 2020-04-04 13:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_auto_20200404_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='logo',
            field=models.ImageField(upload_to='books/logo', verbose_name='Обложка'),
        ),
        migrations.AlterField(
            model_name='news',
            name='date_create',
            field=models.DateField(default=datetime.datetime(2020, 4, 4, 13, 57, 58, 967778), verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='news',
            name='logo',
            field=models.ImageField(null=True, upload_to='News/logo', verbose_name='Обложка'),
        ),
    ]

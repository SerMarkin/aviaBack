# Generated by Django 3.0.4 on 2020-04-04 13:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20200329_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='date_create',
            field=models.DateField(default=datetime.datetime(2020, 4, 4, 13, 10, 21, 23772), verbose_name='Дата публикации'),
        ),
    ]

# Generated by Django 3.1.7 on 2021-04-11 23:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='disciplines',
            new_name='discipline',
        ),
    ]

# Generated by Django 3.1.7 on 2021-04-14 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20210414_2215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='plus_info',
        ),
        migrations.AddField(
            model_name='lesson',
            name='place',
            field=models.CharField(max_length=100, null=True, verbose_name='Место'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='teacher',
            field=models.CharField(max_length=100, null=True, verbose_name='Преподаватель'),
        ),
        migrations.AlterField(
            model_name='discipline',
            name='name',
            field=models.CharField(max_length=200, unique=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='specialgroupname',
            name='short_name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Короткое название'),
        ),
    ]
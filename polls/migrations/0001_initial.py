# Generated by Django 3.1.7 on 2021-04-11 23:02

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('short_name', models.CharField(max_length=200, verbose_name='Короткое название')),
                ('description', models.CharField(max_length=200, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'дисциплина',
                'verbose_name_plural': 'дисциплины',
            },
        ),
        migrations.CreateModel(
            name='GroupStudy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('year_digit', models.IntegerField(verbose_name='Год начала')),
            ],
        ),
        migrations.CreateModel(
            name='KitchenMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_create', models.DateField(default=django.utils.timezone.now, verbose_name='Дата публикации')),
                ('date_actual', models.DateField(verbose_name='На какую дату действует')),
                ('breakfast', models.CharField(max_length=200, verbose_name='Завтрак')),
                ('lunch', models.CharField(max_length=200, verbose_name='Обед')),
                ('dinner', models.CharField(max_length=200, verbose_name='Ужин')),
            ],
            options={
                'verbose_name': 'Расписание столовой',
                'verbose_name_plural': 'Расписание столовой',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('logo', models.ImageField(null=True, upload_to='News/logo', verbose_name='Обложка')),
                ('date_create', models.DateField(default=django.utils.timezone.now, verbose_name='Дата публикации')),
                ('link_source', models.CharField(max_length=300, null=True, verbose_name='Ссылка на первоисточник')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
        migrations.CreateModel(
            name='TimeForLessons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_num', models.IntegerField(unique=True, verbose_name='№')),
                ('time_start', models.TimeField(verbose_name='Начало')),
                ('time_end', models.TimeField(verbose_name='Конец')),
            ],
            options={
                'verbose_name': 'Время занятий',
                'verbose_name_plural': 'Время занятий',
            },
        ),
        migrations.CreateModel(
            name='TimeTableLessons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_create', models.DateField(verbose_name='Дата публикации')),
                ('date_actual', models.DateField(verbose_name='Расписание на')),
            ],
            options={
                'verbose_name': 'Расписание занятий',
                'verbose_name_plural': 'Расписание занятий',
            },
        ),
        migrations.CreateModel(
            name='YearStudy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('year_digit', models.IntegerField(verbose_name='Код')),
            ],
            options={
                'verbose_name': 'год обучения',
                'verbose_name_plural': 'года обучения',
            },
        ),
        migrations.CreateModel(
            name='SpecialGroupName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Полное название группы')),
                ('short_name', models.CharField(max_length=100, verbose_name='Короткое название')),
                ('number_group', models.CharField(max_length=20, verbose_name='Номер группы')),
                ('show_in_menu', models.BooleanField(verbose_name='Показывать/Скрыть в меню')),
                ('year_digit', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='polls.yearstudy')),
            ],
            options={
                'verbose_name': 'Название группы',
                'verbose_name_plural': 'Названия групп',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('plus_info', models.TextField(null=True, verbose_name='Доп информация')),
                ('times_for_lessons', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='polls.timeforlessons', verbose_name='Время')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('author', models.CharField(max_length=200, verbose_name='Автор')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('logo', models.ImageField(upload_to='Books/logo', verbose_name='Обложка')),
                ('src', models.FileField(upload_to='Books/file', verbose_name='Файл')),
                ('disciplines', models.ManyToManyField(to='polls.Discipline')),
            ],
            options={
                'verbose_name': 'Книгa',
                'verbose_name_plural': 'Книги',
            },
        ),
    ]

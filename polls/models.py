from django.db import models
from datetime import datetime
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200,verbose_name="Название")
    description = models.TextField(null=True,verbose_name="Описание")
    logo = models.ImageField(verbose_name="Обложка",upload_to="Books/logo")
    src = models.FileField(verbose_name="Файл",upload_to="Books/file")
    def __str__(self):
        return self.title
    
    class Meta:
         verbose_name = "Книгa"
         verbose_name_plural = "Книги"


class News(models.Model):
    title = models.CharField(max_length=200,verbose_name="Название")
    description = models.TextField(null=True,verbose_name="Описание")
    logo = models.ImageField(verbose_name="Обложка",null=True,upload_to="News/logo")
    date_create = models.DateField(verbose_name="Дата публикации",default=datetime.today())
    link_source = models.CharField(max_length=300,verbose_name="Ссылка на первоисточник",null=True)
    # picts = models.ImageField() TODO : сделать возможность загрузить сразу несколько фото

    def __str__(self):
        return self.title

    class Meta:
         verbose_name = "Новость"
         verbose_name_plural = "Новости"

class KitchenMenu(models.Model):
    date_create = models.DateField(verbose_name="Дата публикации")
    date_actual = models.DateField(verbose_name="На какую дату действует")
    breakfast = models.CharField(max_length=200,verbose_name="Завтрак")
    lunch = models.CharField(max_length=200,verbose_name="Обед")
    dinner = models.CharField(max_length=200,verbose_name="Ужин")


    def __str__(self):
        return f"Расписание столовой №{self.id} на {self.date_actual}"

    class Meta:
         verbose_name = "Расписание столовой"
         verbose_name_plural = "Расписание столовой"




class TimeForLessons(models.Model):
    order_num = models.IntegerField(unique=True,verbose_name="№")
    time_start = models.TimeField(verbose_name="Начало")
    time_end = models.TimeField(verbose_name="Конец")


    def __str__(self):
        return f"Время занятий №{self.id}"


    class Meta:
         verbose_name = "Время занятий"
         verbose_name_plural = "Время занятий"
        



class Lesson(models.Model):
    title = models.CharField(max_length=200,verbose_name="Название")
    plus_info = models.TextField(null=True,verbose_name="Доп информация")
    times_for_lessons=models.OneToOneField(TimeForLessons,on_delete=models.CASCADE,verbose_name="Время")

    def __str__(self):
        return f"№{self.id} {self.title} на {self.times_for_lessons}"


class TimeTableLessons(models.Model):
    date_create = models.DateField(verbose_name="Дата публикации")
    date_actual = models.DateField(verbose_name="Расписание на")

    def __str__(self):
        return f"№{self.id} на {self.date_actual}"


    class Meta:
         verbose_name = "Расписание занятий"
         verbose_name_plural = "Расписание занятий"

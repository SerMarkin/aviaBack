from typing import Set
from django.core.exceptions import ValidationError
from django.db import models
from datetime import datetime
from django.db.models.deletion import CASCADE, SET_NULL
from django.utils import timezone
from django.db.models.signals import post_delete
from django.dispatch import receiver

# Create your models here.

class BaseModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Discipline(BaseModel):
    name = models.CharField(unique=True,max_length=200,verbose_name="Название")
    short_name = models.CharField(max_length=200, verbose_name="Короткое название")
    description = models.CharField(max_length=200, verbose_name="Описание")
    
    def __str__(self):
        return f"№{self.id} {self.name}"

    class Meta:
         verbose_name = "дисциплина"
         verbose_name_plural = "дисциплины"


class Book(BaseModel):
    title = models.CharField(max_length=200,verbose_name="Название")
    author = models.CharField(max_length=200,verbose_name="Автор")
    disciplines = models.ManyToManyField(Discipline)
    description = models.TextField(null=True,verbose_name="Описание")
    logo = models.ImageField(verbose_name="Обложка",upload_to="Books/logo")
    src = models.FileField(verbose_name="Файл",upload_to="Books/file")
    
    def __str__(self):
        return self.title
    
    class Meta:
         verbose_name = "Книгa"
         verbose_name_plural = "Книги"



class News(BaseModel):
    title = models.CharField(max_length=200,verbose_name="Название")
    description = models.TextField(null=True,verbose_name="Описание")
    logo = models.ImageField(verbose_name="Обложка",null=True,upload_to="News/logo")
    date_create = models.DateField(verbose_name="Дата публикации",default=timezone.now)
    link_source = models.CharField(max_length=300,verbose_name="Ссылка на первоисточник",null=True)
    # picts = models.ImageField() TODO : сделать возможность загрузить сразу несколько фото

    def __str__(self):
        return self.title

    class Meta:
         verbose_name = "Новость"
         verbose_name_plural = "Новости"

class KitchenMenu(BaseModel):
    date_create = models.DateField(verbose_name="Дата публикации",default=timezone.now)
    date_actual = models.DateField(verbose_name="На какую дату действует")
    breakfast = models.CharField(max_length=200,verbose_name="Завтрак")
    lunch = models.CharField(max_length=200,verbose_name="Обед")
    dinner = models.CharField(max_length=200,verbose_name="Ужин")


    def __str__(self):
        return f"Расписание столовой №{self.id} на {self.date_actual}"

    class Meta:
         verbose_name = "Расписание столовой"
         verbose_name_plural = "Расписание столовой"




class TimeForLessons(BaseModel):
    order_num = models.IntegerField(unique=True,verbose_name="№")
    time_start = models.TimeField(verbose_name="Начало")
    time_end = models.TimeField(verbose_name="Конец")


    def __str__(self):
        return f"Время занятий №{self.id}"


    class Meta:
         verbose_name = "Время занятий"
         verbose_name_plural = "Время занятий"
        



class Lesson(BaseModel):
    discipline = models.ForeignKey(Discipline,on_delete=CASCADE)
    place = models.CharField(verbose_name="Место",max_length=100,null=True)
    teacher = models.CharField(verbose_name="Преподаватель", max_length=100,null=True)
    times_for_lessons=models.ForeignKey(TimeForLessons,on_delete=models.CASCADE,verbose_name="Время")

    class Meta:
         verbose_name = "Пара"
         verbose_name_plural = "Пары"

    def __str__(self):
        return f"№{self.id} {self.discipline} на {self.times_for_lessons}"
    
class YearStudy(BaseModel):
    name = models.CharField(max_length=100,verbose_name="Название")
    year_digit = models.IntegerField(verbose_name="Код")
    
    class Meta:
         verbose_name = "год обучения"
         verbose_name_plural = "года обучения"
    def __str__(self):
        return self.name

class SpecialGroupName(BaseModel):
    name = models.CharField(max_length=200,verbose_name="Полное название группы")
    short_name = models.CharField(unique=True,max_length=100,verbose_name="Короткое название")
    year_digit = models.ForeignKey(YearStudy,on_delete=models.CASCADE)
    number_group = models.CharField(max_length=20, verbose_name="Номер группы")
    show_in_menu = models.BooleanField(verbose_name="Показывать/Скрыть в меню")

    class Meta:
         verbose_name = "Название группы"
         verbose_name_plural = "Названия групп"
    
    def __str__(self):
        return self.name


class StudyDay(BaseModel):
    date_actual = models.DateField(verbose_name="Дата")
    group = models.ForeignKey(SpecialGroupName,on_delete=models.CASCADE)
    lessons = models.ManyToManyField(Lesson)

    class Meta:
         verbose_name = "Учебный день"
         verbose_name_plural = "Учебные дни"

    def delete(self, *args, **kwargs):
        Lesson.objects.filter(id__in=[t.id for t in self.lessons]).delete()
        self.lessons.remove()
        super(StudyDay, self).delete(*args, **kwargs)

    def __str__(self):
        return f"Учебный день на {self.date_actual} для {self.group.short_name}"


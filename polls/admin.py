from django.contrib import admin

# Register your models here.

from .models import Book, KitchenMenu, Lesson, TimeForLessons, TimeTableLessons

admin.site.register(Book)
admin.site.register(KitchenMenu)
admin.site.register(Lesson)
admin.site.register(TimeForLessons)
admin.site.register(TimeTableLessons)
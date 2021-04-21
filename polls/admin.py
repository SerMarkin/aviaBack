from django.contrib import admin
from django.http import HttpResponseRedirect
from django.conf.urls import url
# Register your models here.

from .models import Book, KitchenMenu, Lesson, TimeForLessons, Discipline,  SpecialGroupName, YearStudy, StudyDay, News

admin.site.register(Book)
admin.site.register(KitchenMenu)
admin.site.register(TimeForLessons)
admin.site.register(Discipline)
admin.site.register(SpecialGroupName)
admin.site.register(YearStudy)
admin.site.register(News)



class StudyDayAdmin(admin.ModelAdmin):
    
    def save_model(self, request, obj, form, change) -> None:
        #Добавить невозможность добавления на уже существующую дату
        return super().save_model(request, obj, form, change)



admin.site.register(StudyDay,StudyDayAdmin)

class LessonAdmin(admin.ModelAdmin):
    change_list_template = "admin/import_from_xlsx.html"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            url(
                r'^lesson/import/$',
                self.admin_site.admin_view(self),
                name='lesson-import',
            )
        ]
        return custom_urls + urls



admin.site.register(Lesson,LessonAdmin)

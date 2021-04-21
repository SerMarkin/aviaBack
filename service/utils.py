from csv import DictReader
from io import StringIO
from django.db import transaction
from django.core.exceptions import ValidationError
from polls.models import Lesson, Discipline, StudyDay, SpecialGroupName, TimeForLessons
from datetime import datetime
import logging

def get_and_parse_file(file):
    print(file)
    reader = DictReader(StringIO(file.read().decode("utf-8-sig")),delimiter=';')
    mappingDays = {}
    indexRow = 1
    for row in reader:
        print(row)
        indexRow += 1
        group = SpecialGroupName.objects.filter(short_name=row['группа']).first()
        hour = TimeForLessons.objects.filter(order_num=row['час']).first()
        dicp = Discipline.objects.filter(name = row['дисциплина']).first()
        date = row['дата']
        place = row['место']
        teacher = row['преподаватель']
        if (group == None or date == None or hour == None or dicp == None or date==''):
            print(f"no data {group == None} {date == None} {hour == None} {dicp == None} {date==''}")
            raise ValidationError(message=f"Не правильная строка №{indexRow}")
        date = datetime.strptime(date, "%d.%m.%Y").date()
        if (not (group in mappingDays)):
            mappingDays[group] = {}
        if (not (date in mappingDays[group])):
            mappingDays[group][date] = []
        mappingDays[group][date].append({"teacher":teacher,"dicp":dicp,"place":place,"hour":hour})
    save_study_days(mappingDays=mappingDays)
        # lesson = Lesson.objects.get_or_create(teacher=teacher,discipline=dicp,place=place,times_for_lessons=hour)
        # study_day = StudyDay.objects.create(date_actual=date)
        # study_day.group.set([group])
        # study_day.lessons.set([lesson])
        # study_day.save()

def save_study_days(mappingDays):
    def lesson_creator(map_study_lesson): 
        lesson = Lesson.objects.create(teacher=map_study_lesson["teacher"],discipline=map_study_lesson["dicp"],place=map_study_lesson["place"],times_for_lessons=map_study_lesson["hour"])
        return lesson
    try:
        for group in mappingDays:
            for date in mappingDays[group]:
                StudyDay.objects.filter(group=group,date_actual=date).delete()
                new_study_day = StudyDay.objects.create(date_actual=date,group=group)
                lessons = list(map(lesson_creator,mappingDays[group][date]))
                new_study_day.lessons.set(lessons)
    except BaseException as ex:
        logging.exception(ex)

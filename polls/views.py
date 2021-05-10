from django.shortcuts import redirect, render

from django.http import HttpResponse

from django.conf.urls import url, include
from rest_framework import routers, serializers, generics
from polls.models import Book, Discipline, Lesson, StudyDay, SpecialGroupName, TimeForLessons, YearStudy
from service.utils import get_and_parse_file


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()

# Serializers define the API representation.
class DisciplineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Discipline
        fields = ['name', 'description', 'short_name']

class BookSerializer(serializers.HyperlinkedModelSerializer):
    disciplines = DisciplineSerializer(many=True)
    logo_url = serializers.SerializerMethodField()
    src_url = serializers.SerializerMethodField()
    class Meta:
        model = Book
        fields = ['title', 'description', 'logo_url','src_url','author','disciplines']

    def get_logo_url(self,book):
        logo_url = book.logo.url
        return logo_url

    def get_src_url(self,book):
        src_url = book.src.url
        return src_url

# ViewSets define the view behavior.
class BookPostsReadView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    model = serializer_class.Meta.model

class TimeForLessonsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TimeForLessons
        fields = ['order_num','time_start','time_end']

class LessonsSerializer(serializers.ModelSerializer):
    discipline = DisciplineSerializer
    times_for_lessons = TimeForLessonsSerializer
    class Meta:
        model = Lesson
        fields = ['id','place', 'teacher', 'times_for_lessons','discipline']
        depth = 4

class YearStudySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = YearStudy
        fields = ['id','name',  'year_digit']

class YearStudyReadView(generics.ListAPIView):
    queryset = YearStudy.objects.all()
    serializer_class = YearStudySerializer
    model = serializer_class.Meta.model



class SpecialGroupNameSerializer(serializers.ModelSerializer):
    year_digit = YearStudySerializer
    class Meta:
        model = SpecialGroupName
        fields = ['id','name', 'short_name', 'year_digit','number_group','show_in_menu']


class SpecialGroupNameReadView(generics.ListAPIView):
    serializer_class = SpecialGroupNameSerializer
    model = serializer_class.Meta.model

    def get_queryset(self):
        return SpecialGroupName.objects.filter(show_in_menu=True)


# Serializers define the API representation.
class StudyDaySerializer(serializers.ModelSerializer):
    lessons = LessonsSerializer(many=True)
    group = SpecialGroupNameSerializer
    class Meta:
        model = StudyDay
        fields = ['id','date_actual', 'group', 'lessons']
        depth = 4

class StudyDaysReadView(generics.ListAPIView):
    serializer_class = StudyDaySerializer
    model = serializer_class.Meta.model

    def get_queryset(self):
        number_week = self.request.query_params.get('number_week')
        group_short_name = self.request.query_params.get('group_short_name')
        if (number_week == None) or (group_short_name == None):
            return []
        p = StudyDay.objects.all().filter(date_actual__week=number_week).filter(group__short_name=group_short_name)
        return p



def index(request):
    get_and_parse_file(request.FILES['файл'])
    return redirect(to="/admin/polls/studyday/")



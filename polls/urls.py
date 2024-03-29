"""aviaBack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from . import views
from django.conf.urls import url, include

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^', include(views.router.urls)),
    path('books', views.BookPostsReadView.as_view(), name='books'),
    path('studydays', views.StudyDaysReadView.as_view(), name='studydays'),
    path('yearstudy', views.YearStudyReadView.as_view(), name='yearstudy'),
    path('groups', views.SpecialGroupNameReadView.as_view(), name='groups'),
    path('import', views.index)
]

from django.shortcuts import render

from django.http import HttpResponse

from django.conf.urls import url, include
from rest_framework import routers, serializers, generics
from polls.models import Book



# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()

# Serializers define the API representation.
class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'description', 'logo','src']

# ViewSets define the view behavior.
class BookPostsReadView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    model = serializer_class.Meta.model



def index(request):
    return HttpResponse("Its work")



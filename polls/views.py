from django.shortcuts import render

from django.http import HttpResponse

from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets
from polls.models import Book



# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()

# Serializers define the API representation.
class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'description', 'logo','src']

# ViewSets define the view behavior.
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

router.register(r'books', BookViewSet)

def index(request):
    return HttpResponse("Its work")



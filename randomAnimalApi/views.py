# views for randomAnimalApi app
from rest_framework import viewsets

from randomAnimalApi.models import AnimalMeme, MemeTag
from randomAnimalApi.serializers import AnimalMemeSerializer, MemeTagSerializer


class MemeTagViewSet(viewsets.ModelViewSet):
    queryset = MemeTag.objects.all()
    serializer_class = MemeTagSerializer


class AnimalViewSet(viewsets.ModelViewSet):
    queryset = AnimalMeme.objects.all()
    serializer_class = AnimalMemeSerializer

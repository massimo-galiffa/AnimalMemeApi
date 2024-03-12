from rest_framework.routers import DefaultRouter
from django.urls import include, path

from . import views

router = DefaultRouter(trailing_slash=False)
router.register(r'RandomAnimalMemes', views.AnimalViewSet)

from django.contrib import admin

# Register your models here.
from .models import AnimalMeme, MemeTag

admin.site.register(AnimalMeme)
admin.site.register(MemeTag)

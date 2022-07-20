from operator import imod
from django.contrib import admin
from . models import City
from .models import addNotes


admin.site.register(City)
admin.site.register(addNotes)

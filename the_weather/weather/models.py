from tabnanny import verbose
import django
from django.db import models


#add notes to database django admin
class addNotes(models.Model):
    notes = models.CharField(max_length=200)

    def __str__(self):
        return self.notes

    class Meta:
        verbose_name_plural = 'Notes'


class City(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'cities'

from django.db import models
from django.db.models.fields import CharField, TextField
from django.db.models.fields.files import ImageField

# Create your models here.
class Carosual(models.Model):
    short_description = models.TextField()
    image  = models.ImageField(upload_to='media/')
    

    def __str__(self):
        return self.short_description


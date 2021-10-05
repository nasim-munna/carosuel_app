from django.db import models
from django.db.models.fields import CharField, TextField
from django.db.models.fields.files import ImageField

# Create your models here.
class Carosuel(models.Model):
    title = models.CharField(max_length=50)
    short_description = models.TextField()
    image  = models.ImageField(upload_to='media/')
    creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


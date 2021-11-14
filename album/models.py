from django.db import models
from django.urls import reverse
# Create your models here.
class Album(models.Model):

    title = models.CharField(max_length=50)
    short_description = models.TextField()

    image = models.ImageField(upload_to='album/')
    creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
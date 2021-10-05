from django.contrib import admin
from .models import Carosuel
# Register your models here.
class CarosuelAdmin(admin.ModelAdmin):

    list_display= ['title','image']
    search_fields = ['title']

admin.site.register(Carosuel, CarosuelAdmin)
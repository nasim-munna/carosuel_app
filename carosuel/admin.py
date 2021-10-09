from django.contrib import admin
from .models import Carosual
# Register your models here.
class CarosuelAdmin(admin.ModelAdmin):

    list_display= ['short_description','image']
    search_fields = ['short_description']

admin.site.register(Carosual, CarosuelAdmin)
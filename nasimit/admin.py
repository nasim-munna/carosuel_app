from django.contrib import admin
from .models import Expert,Project,Testimonials
# Register your models here.
class ExpertAdmin(admin.ModelAdmin):
    list_display = ['name','image','designation']
    search_fields = ['name']

admin.site.register(Expert,ExpertAdmin)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name','image','category']
    search_fields = ['name']

admin.site.register(Project,ProjectAdmin)

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name','image']

admin.site.register(Testimonials,TestimonialAdmin)
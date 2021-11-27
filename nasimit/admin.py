from django.contrib import admin
from .models import Expert,Project,Testimonials,Service,Partner,Award ,Appointment,Contact,Post
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

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name','image']

admin.site.register(Service,ServiceAdmin)

class PartnerAdmin(admin.ModelAdmin):
    list_display = ['image','hover_image']

admin.site.register(Partner,PartnerAdmin)

class AwardAdmin(admin.ModelAdmin):
    list_display = ['image','name']

admin.site.register(Award,AwardAdmin)

class AppoinmentAdmin(admin.ModelAdmin):
    list_display = ['name','email','department']

admin.site.register(Appointment,AppoinmentAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','email','department','message']

admin.site.register(Contact,ContactAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
  
admin.site.register(Post, PostAdmin)


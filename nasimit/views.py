from django.shortcuts import render
from .models import Expert,Project, Testimonials
# Create your views here.
def index(request):
    experts = Expert.objects.all()
    projects = Project.objects.all()
    testimonials = Testimonials.objects.all()
    context = {
        'experts':experts,
        'projects':projects,
        'testimonials':testimonials
    }
    return render(request,'nasimit/nasimit.html',context)
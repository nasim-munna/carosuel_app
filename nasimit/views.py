from django.shortcuts import render,get_object_or_404
from .forms import AppointmentForm,ContactForm
from django.http import HttpResponseRedirect
from .models import Award, Expert,Project, Testimonials,Service,Partner,Award,Appointment,Post
from django.views.generic.edit import FormView
from django.views import generic
# Create your views here.
def index(request):
    experts = Expert.objects.all()
    projects = Project.objects.all()
    testimonials = Testimonials.objects.all()
    services = Service.objects.all()
    partners = Partner.objects.all()
    awards =Award.objects.all()

    if request.method == 'POST':
        
        appointment_form = AppointmentForm(request.POST)
        
        if appointment_form.is_valid():
            
            appointment_form.save()
            # redirect to a new URL:
            return HttpResponseRedirect(request.path_info)

    
    
    
    # if a GET (or any other method) we'll create a blank form
    else:
        
        appointment_form = AppointmentForm()
    context = {
        'experts':experts,
        'projects':projects,
        'testimonials':testimonials,
        'services':services,
        'partners':partners,
        'awards':awards
    }
    return render(request,'nasimit/nasimit.html',context)

def contact(request):

    if request.method == 'POST':
        
        contact_form = ContactForm(request.POST)
        
        
        if contact_form.is_valid():
            
            contact_form.save()
           
            # redirect to a new URL:
            return HttpResponseRedirect('/')
        
        
    
    # if a GET (or any other method) we'll create a blank form
    else:
        contact_form = ContactForm()
        
    
    context = {

    }

    return render(request, 'nasimit/nasimit.html', context)

def itsolution(request):
    return render (request,'nasimit/itsolution.html')

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'nasimit/index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'nasimit/post_detail.html'
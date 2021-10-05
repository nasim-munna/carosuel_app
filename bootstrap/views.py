from django.shortcuts import render
from .models import Carosuel
# Create your views here.
def index(request):
    carosuel_data = Carosuel.objects.all()
    context = {
        'carosuel_data': carosuel_data
    }
    return render(request,'index.html',context)
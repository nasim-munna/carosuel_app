from django.shortcuts import render
from .models import Carosual
# Create your views here.
def index(request):
    carosuel_data = Carosual.objects.all()
    context = {
        'carosuel_data': carosuel_data
    }
    return render(request,'carosuel/index.html',context)
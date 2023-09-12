from django.shortcuts import render
from .models import Institution_info

# Create your views here.

def index(request):
    institution_info = Institution_info.objects.all()
    
    context ={
            'institution_info':institution_info
        }
    
    return render(request, 'main_app/index.html', context)

def classRoutine(request):
    return render(request, 'main_app/classRoutine.html')
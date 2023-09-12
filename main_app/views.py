from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    institution_info = Institution_info.objects.all()
    
    context ={
            'institution_info':institution_info
        }
    
    return render(request, 'main_app/index.html', context)

def classRoutine(request):
    return render(request, 'main_app/classRoutine.html')

def notices(request):
    notice = Notice.objects.all().order_by("-id")
    
    context = {
        'notice': notice
        }
    return render(request, 'main_app/notices.html',context)

def managing_committee(request):
    managing = Managing_committee.objects.all()
    
    context = {
        'managing': managing
        }
    return render(request, 'main_app/managing_committee.html',context)
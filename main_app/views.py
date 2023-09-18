from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth import *

# Create your views here.

def index(request):
    institution_info = Institution_info.objects.all()
    
    context ={
            'institution_info':institution_info
        }
    
    return render(request, 'main_app/index.html', context) 

def classRoutine(request):
    routine = ClassRoutine.objects.all().order_by("-id")
    context = {
        'routine': routine
        }
    return render(request, 'main_app/classRoutine.html',context)

def notices(request):
    notice = Notice.objects.all().order_by("-id")
    
    context = {
        'notice': notice
        }
    return render(request, 'main_app/notices.html',context)

def managing_committee(request):
    managing = Managing_committee.objects.all().exclude(ordering=1)
    head = Managing_committee.objects.get(ordering=1)
    
    context = {
        'managing': managing,
        'head': head
        }
    return render(request, 'main_app/managing_committee.html',context)

def teacher(request):
    teacher_all = Teacher.objects.all().exclude(ordering=1)
    teacher_h = Teacher.objects.get(ordering=1)
    
    context = {
        'teacher_h': teacher_h,
        'teacher_all': teacher_all
        }
    return render(request, 'main_app/teacher.html',context)



def photoGallery(request):
    photo_g = Photo_gallery.objects.all()
    context={
        'photo_g':photo_g
    }
    return render(request, 'main_app/photoGallery.html',context)

    
def video_gallery(request):
    video_g = Video_gallery.objects.all()
    context={
        'video_g':video_g
    }
    return render(request, 'main_app/videoGallery.html',context)

def result(request):
    results = Result.objects.all().order_by('-id')

    context = {
        'results': results
        }
    return render(request, 'main_app/result.html', context)

def students_info(request):
    if request.method == 'GET':
        class_name = request.GET.get('class')
        print(class_name)
        if class_name:
            students = Add_Student_info.objects.filter(select_class=class_name)
            print(students)
        else:
            students = Add_Student_info.objects.all()
            print(students)
  
    context = {
        'students': students,
    }
    return render(request, 'main_app/student_info.html', context)

def contact(request):
    addres = Contatc_address.objects.all() 
    forms = ContactForm(request.POST)
    if request.method == 'POST':
        forms = ContactForm(request.POST)
        print(forms)
        if forms.is_valid():
            forms.save()
            return redirect('contact')
        else:
            forms =ContactForm()
            return render(request,'userapp/contact.html') 
    context = {
        'forms': forms,
        'addres': addres
        }    
    return render(request, 'main_app/contact.html', context)

def admission(request):
    return render(request, 'main_app/admission.html')

def blog(request):
    return render(request, 'main_app/blog.html')



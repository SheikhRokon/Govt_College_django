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
    return render(request, 'main_app/result.html',context)

def students_info(request):
    one = Add_Student_info.objects.filter(select_class='class_1').order_by('id')
    two = Add_Student_info.objects.filter(select_class='class_2').order_by('id')
    three = Add_Student_info.objects.filter(select_class='class_3').order_by('id')
    four = Add_Student_info.objects.filter(select_class='class_4').order_by('id')
    five = Add_Student_info.objects.filter(select_class='class_5').order_by('id')
    six = Add_Student_info.objects.filter(select_class='class_6').order_by('id')
    seven = Add_Student_info.objects.filter(select_class='class_7').order_by('id')
    eight = Add_Student_info.objects.filter(select_class='class_8').order_by('id')
    nine = Add_Student_info.objects.filter(select_class='class_9').order_by('id')
    ten = Add_Student_info.objects.filter(select_class='class_10').order_by('id')
    inter_1 = Add_Student_info.objects.filter(select_class='inter_first_year').order_by('id')
    inter_2 = Add_Student_info.objects.filter(select_class='inter_second_year').order_by('id')
    context = {
        'one': one,
        'two': two,
        'three': three,
        'four': four,
        'five': five,
        'six': six,
        'seven':seven,
        'eight': eight,
        'nine': nine,
        'ten': ten,
        'inter_1': inter_1,
        'inter_2': inter_2,
    }
    return render(request, 'main_app/student_info.html', context)
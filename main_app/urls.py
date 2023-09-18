from django.urls import path
from .views import * 



urlpatterns = [
     path('',index ,name='index'),
     path('classRoutine/',classRoutine ,name='classRoutine'),
     path('notices/',notices ,name='notices'),
     path('managing_committee/',managing_committee ,name='managing_committee'),
     path('teachers/',teacher ,name='teachers'),
     path('photoGallery/',photoGallery ,name='photoGallery'),
     path('video_gallery/',video_gallery ,name='video_gallery'),
     path('result/',result ,name='result'),
     path('students_info/',students_info ,name='students_info'),
     path('contact/',contact ,name='contact'),
     path('admission/',admission ,name='admission'),
     path('blog/',blog ,name='blog'),
]
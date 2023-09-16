from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone

# Create your models here.
class Institution_info(models.Model):
    banners_image = models.ImageField(upload_to='banner_image')
    principal_name = models.CharField(max_length=200)
    vice_principal_name = models.CharField(max_length=200)
    principal_image = models.ImageField(upload_to='principal_image')
    vice_principal_image = models.ImageField(upload_to='vice_principal_image')
    institution_image = models.ImageField(upload_to='institution_image')
    news = RichTextUploadingField()
    principal_message = RichTextUploadingField()
    vice_principal_message = RichTextUploadingField()
    institution_history = RichTextUploadingField()
    
    class Meta:
        verbose_name = 'Institution info'
        verbose_name_plural = 'Institution info'

    def __str__(self):
        return self.principal_name
    

class Notice(models.Model):
    title = models.CharField(max_length=500)
    date = models.DateTimeField(default=timezone.now)
    notice_file = models.FileField(upload_to='notices/')
    

    class Meta:
        verbose_name = 'Notice'
        verbose_name_plural = 'Notice'

    def __str__(self):
        return self.title


class Managing_committee(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    image = models.ImageField(upload_to='managing_committee_image')
    ordering  = models.IntegerField(unique=True,blank=True,null=True)

    class Meta:
        verbose_name = "Managing committee"
        verbose_name_plural = "Managing committees"

    def __str__(self):
        return self.name
    
class Teacher(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    image = models.ImageField(upload_to='Teacher_image')
    ordering  = models.IntegerField(unique=True,blank=True,null=True)

    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = "Teacher"

    def __str__(self):
        return self.name
    
    
    
class Photo_gallery(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='p_image')
   

    class Meta:
        verbose_name_plural = 'Photo gallery'

    def __str__(self):
        return str(self.title)

class Video_gallery(models.Model):
    title = models.CharField(max_length=150)
    youtube_link = models.URLField(max_length=200,blank=True)

    class Meta:
        verbose_name_plural = 'Video gallery'

    def __str__(self):
        return str(self.title)  
    

class Result(models.Model):
    title = models.CharField(max_length=500)
    date = models.DateTimeField(default=timezone.now)
    result_file = models.FileField(upload_to='result/', blank=True, null=True)
    board_result_link = models.URLField(max_length=200,blank=True, null=True)
    

    class Meta:
        verbose_name = 'Result'
        verbose_name_plural = 'Result'

    def __str__(self):
        return self.title 

class ClassRoutine(models.Model):
    title = models.CharField(max_length=500)
    routine_file = models.FileField(upload_to='result/')
    class Meta:
        verbose_name = 'Class Routine'
        verbose_name_plural = 'Class Routine'

    def __str__(self):
        return self.title
    
class Add_Student_info(models.Model):
    Class_Name =(
        ('class_1','class_1'),
        ('class_2','class_2'),
        ('class_3','class_3'),
        ('class_4','class_4'),
        ('class_5','class_5'),
        ('class_6','class_6'),
        ('class_7','class_7'),
        ('class_8','class_8'),
        ('class_9','class_9'),
        ('class_10','class_10'),
        ('inter_first_year','inter_first_year'),
        ('inter_second_year','inter_second_year'),
    )
    select_class = models.CharField(max_length=200,choices=Class_Name)
    student_class_roll = models.IntegerField()
    student_name = models.CharField(max_length=200)
    student_image = models.ImageField(upload_to='student_image')
    guardian_number_1 = models.CharField(max_length=15, blank=True, null=True)
    guardian_number_2 = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    Section =(
        ('ক','ক'),
        ('খ','খ'),
        ('গ','গ'),
        ('ঘ','ঘ'),
        ('ঙ','ঙ'),
        ('চ','চ'),
        ('ছ','ছ'),
    )
    select_sections = models.CharField(max_length=5,choices=Section)

    class Meta:
        verbose_name_plural = 'Add Student info'
        ordering = ['student_class_roll']

    def __str__(self):
        return self.student_name + ' (' + self.select_class +')' + '( ' + self.select_sections + ' )'
    
             



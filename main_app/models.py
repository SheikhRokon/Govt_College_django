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
        verbose_name = 'Institution_info'
        verbose_name_plural = 'Institution_infos'

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
        verbose_name = "Managing_committee"
        verbose_name_plural = "Managing_committees"

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



from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

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

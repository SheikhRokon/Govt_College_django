from django.db import models

# Create your models here.
class Institution_info(models.Model):
    banners_image = models.ImageField(upload_to='banner_image')
    news = models.CharField(max_length=1500)
    principal_name = models.CharField(max_length=200)
    vice_principal_name = models.CharField(max_length=200)
    principal_image = models.ImageField(upload_to='principal_image')
    vice_principal_image = models.ImageField(upload_to='vice_principal_image')
    principal_message = models.CharField(max_length=1500)
    vice_principal_message = models.CharField(max_length=1500)
    institution_history = models.CharField(max_length=2000)
    institution_image = models.ImageField(upload_to='institution_image')
    
    class Meta:
        verbose_name = 'Institution_info'
        verbose_name_plural = 'Institution_infos'

    def __str__(self):
        return self.principal_name

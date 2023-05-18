from django.db import models

# Create your models here.
class Feature(models.Model):
    name = models.CharField(max_length=200,default='SOME STRING')
    details = models.CharField(max_length=500,default='SOME STRING')

    def _str_(self):
        return self.name

    
class Services(models.Model):
    name = models.CharField(max_length=200,default='SOME STRING')
    details = models.CharField(max_length=500,default='SOME STRING')

    def _str_(self):
        return self.name
    
class Team (models.Model):
    name = models.CharField(max_length=200,default='SOME STRING')
    position = models.CharField(max_length=200,default='SOME STRING')
    details = models.CharField(max_length=500,default='SOME STRING')
    image = models.ImageField(upload_to='pics',default='SOME STRING')
    
    def _str_(self):
        return self.name
    

     
from django.db import models
# from django.contrib.auth.models import*
# from .models import AboutAdmin
# Create your models here.

class Contact_Us(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, default="", blank=True)
    message = models.TextField()

    def __str__(self):
        return self.name

class AboutFounder(models.Model):
    Title = models.CharField(max_length=225)
    description = models.TextField()
    image = models.ImageField(upload_to='Image/')

class Articlespage(models.Model):
   Title = models.CharField(max_length=225)
   description = models.TextField()
   image = models.ImageField(upload_to='Image/')
  
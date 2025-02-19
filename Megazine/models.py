from django.db import models

# Create your models here.
# class Contact_Us(models.Model):
#     name=models.charField(max_length=50)
#     phone=models.charField(max_length=50)
#     emails=models.charField(max_length=50)
#     message=models.TextField()
class Contact_Us(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=15)
    message = models.TextField()

    def __str__(self):
        return self.name
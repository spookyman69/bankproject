from django.db import models


# Create your models here.
class Application(models.Model):
    name= models.CharField(max_length=250)
    dob= models.CharField(max_length=250)
    age = models.IntegerField()
    gender = models.CharField(max_length=250)
    phone = models.IntegerField()
    mail = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    district = models.CharField(max_length=250)
    branch = models.CharField(max_length=250)
    acctype = models.CharField(max_length=250)

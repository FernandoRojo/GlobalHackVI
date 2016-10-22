from django.db import models

# Create your models here.
class Shelter(models.Model):
    Name = models.CharField(max_length=200,default="")
    Address = models.CharField(max_length=100);
    Phone = models.CharField(max_length=100);
    Specialty = models.CharField(max_length=100);
    maxCap = models.IntegerField(default = 0);
    foodAvailable = models.BooleanField()
    shelterAvailable = models.BooleanField()
    hygenicAvailable = models.BooleanField()
    counselingAvailable = models.BooleanField()
    otherAvailable = models.BooleanField()
    otherDetails = models.CharField(max_length=500)
    latitude = models.DecimalField(max_digits=9,decimal_places=6)
    longitude = models.DecimalField(max_digits=9,decimal_places=6)

from django.db import models

# Create your models here.
class Item(models.Model):
    Title = models.CharField(max_length=100,default="request")
    description = models.CharField(max_length=300)
    pub_date = models.DateTimeField('date published')

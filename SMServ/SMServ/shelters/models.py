# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Shelter(models.Model):
    name = models.CharField(db_column='Name', max_length=200)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=100)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=100)  # Field name made lowercase.
    maxcap = models.IntegerField(db_column='maxCap')  # Field name made lowercase.
    foodavailable = models.IntegerField(db_column='foodAvailable', blank=True, null=True)  # Field name made lowercase.
    shelteravailable = models.IntegerField(db_column='shelterAvailable', blank=True, null=True)  # Field name made lowercase.
    hygenicavailable = models.IntegerField(db_column='hygenicAvailable', blank=True, null=True)  # Field name made lowercase.
    counselingavailable = models.IntegerField(db_column='counselingAvailable', blank=True, null=True)  # Field name made lowercase.
    otherdetails = models.CharField(db_column='otherDetails', max_length=500)  # Field name made lowercase.
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    email = models.CharField(db_column='Email', max_length=100)  # Field name made lowercase.
    place_id = models.CharField(max_length=40)
    description = models.CharField(db_column='Description', max_length=100)  # Field name made lowercase.
    currcap = models.IntegerField(db_column='currCap')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Shelters_shelter'


class RssfeedItem(models.Model):
    description = models.CharField(max_length=300)
    pub_date = models.DateTimeField()
    title = models.CharField(db_column='Title', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'rssfeed_item'

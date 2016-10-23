from django.contrib import admin

# Register your models here.

from .models import Shelter,Request

admin.site.register(Shelter)
admin.site.register(Request)

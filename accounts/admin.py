from django.contrib import admin
from . models import *
# Register your models here.

class deptAdmin(admin.ModelAdmin):
    list_display=['name']

admin.site.register(depart,deptAdmin)
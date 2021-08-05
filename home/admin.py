from django.contrib import admin
from . models import *

# Register your models here.

admin.site.register(banner)

class categadmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}

admin.site.register(categ,categadmin)

class productadmin(admin.ModelAdmin):
    list_display=['name','price','stock']
    list_editable=['price']
    prepopulated_fields={'slug':('name',)}

admin.site.register(product,productadmin)


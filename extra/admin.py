from django.contrib import admin
from . models import *
# Register your models here.

admin.site.register(cart)

class cartAdmin(admin.ModelAdmin):
    list_display=['prod','ct']


admin.site.register(cartitem,cartAdmin)
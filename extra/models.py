from django.db import models
from home.models import *
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1,on_delete=models.CASCADE,)
    cart_id=models.CharField(max_length=250)
    date_added=models.DateField(auto_now_add=True)

    class Meta:
        db_table='cart'
        ordering=['date_added']



class cartitem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1,on_delete=models.CASCADE,)    
    prod=models.ForeignKey(product,on_delete=models.CASCADE)
    ct=models.ForeignKey(cart,on_delete=models.CASCADE)
    quan=models.IntegerField()
    active=models.BooleanField(default=True)

    class Meta:
        db_table='cartitem'

    def total(self):
        return self.prod.price*self.quan



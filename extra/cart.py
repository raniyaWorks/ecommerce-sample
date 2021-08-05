from decimal import Decimal
from django.conf import settings 
from home.models import *
class cart_create(object):
    def __init__(self,request):
        self.session=request.session
        crt=self.session.get(settings.CART_SESSION_ID)
        if not crt:
            crt=self.session[settings.CART_SESSION_ID]={}
        self.crt=crt

    def add(self,prod,quantity=1,override_quantity=False):
        prod_id=str(product.id)
        if prod_id not in self.crt:
            self.crt[prod_id]={'quantity':0,'price':str(prod.price)}

        if override_quantity:
            self.crt[prod_id]['quantity']=quantity

        else:
            self.crt[prod_id]['quantity']+=quantity
        self.save()

    def save(self):
        self.session.modified=True
    def remove(self,prod):
        prod_id=str(product.id)
        if prod_id in self.crt:
            del self.crt[prod_id]
            self.save()

    def __iter__(self):
        prod_ids=self.crt.keys()
        products=product.objects.filter(id__in==prod_ids)

        crt=self.crt.copy()
        for p in products:
            crt[str(product.id)]['product']=prodt 

        for itm in crt.values():
            itm['price']=Decimal(item['price'])
            itm['total_price']=itm['price']*itm['quantity']
            yield itm

        def __len__(self):
            return sum(itm['quantity'] for i in self.crt.values())

        def get_total_price(self):
            return sum(Decimal(itm['price']*itm['quantity'] for i in self.crt.values))
            
        def clear(self):
            del self.session[settings.CART_SESSION_ID]
            self.save()
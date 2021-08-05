from . models import *
from . views import *



def cnt(request):
    item_count=0
    if 'admin' in request.path:
        return {}
    else:
        try:
            ct=cart.objects.filter(cart_id=ct_id(request))
            cti=cartitem.objects.all().filter(ct=ct[:1])
            for c in cti:
                item_count+=c.quan

        except cart.DoesNotExist:
            item_count=0
        return dict(itcnt=item_count)    
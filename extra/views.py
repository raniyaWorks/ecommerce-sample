from django.shortcuts import render,redirect,get_object_or_404
from django.db.models import Q 
from home.models import *
from . models import *
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def search(request):
    prod=None
    query=None

    if 'q' in request.GET:
        query=request.GET.get('q')
        prod=product.objects.all().filter(Q(name__contains=query)|Q(desc__contains=query))
    return render(request,'search.html',{'query':query,'pr':prod})


def ct_id(request):
    ct=request.session.session_key

    if not ct:
        ct=request.session.create()
    return ct 

def add_cart(request,product_id):
    prod=product.objects.get(id=product_id)
    try:
        ct=cart.objects.get(cart_id=ct_id(request),user=request.user)
        
    except cart.DoesNotExist:
        ct=cart.objects.create(cart_id=ct_id(request))
        ct.user=request.user
        ct.save()
    try:
        ct_item=cartitem.objects.get(prod=prod,ct=ct)
        if ct_item.quan < ct_item.prod.stock:
            ct_item.quan+=1
        ct.user=request.user
        ct_item.save()
    except cartitem.DoesNotExist:
        ct_item=cartitem.objects.create(prod=prod,quan=1,ct=ct)
        ct.user=request.user
        ct_item.save()
    return redirect('cart_details')

def cart_list(request,tot=0,c=0,ct_itms=None):
    try:
        ct=cart.objects.get(cart_id=ct_id(request))
        ct_itms=cartitem.objects.filter(ct=ct,active=True)
        for it in ct_itms:
            tot +=(it.prod.price*it.quan)
            c+=it.quan
    except ObjectDoesNotExist:
        pass

    return render(request,'cart.html',{'ci':ct_itms,'t':tot,'cn':c})

def cart_remove(request,product_id):
    ct=cart.objects.get(cart_id=ct_id(request))
    prod=get_object_or_404(product,id=product_id)
    ct_item=cartitem.objects.get(prod=prod,ct=ct)
    if ct_item.quan>1:
        ct_item.quan-=1
        ct_item.save()

    else:
        ct_item.delete()
    return redirect('cart_details')


def item_remove(request,product_id):
    ct=cart.objects.get(cart_id=ct_id(request))
    prod=get_object_or_404(product,id=product_id)
    ct_item=cartitem.objects.get(prod=prod,ct=ct)
    ct_item.delete()
    return redirect('cart_details')
from django.shortcuts import render,redirect,get_object_or_404
from . models import *
from django.core.paginator import Paginator,EmptyPage,InvalidPage

# Create your views here.

def home(request,c_slug=None):
    ban=banner.objects.all()

    c_page=None
    prod=None

    if c_slug!=None:
        c_page=get_object_or_404(categ,slug=c_slug)
        prod=product.objects.filter(category=c_page,available=True)
    else:
        prod=product.objects.all().filter(available=True)
    links=categ.objects.all()
    paginator=Paginator(prod,6)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        pro=paginator.page(page)
    except(EmptyPage,InvalidPage):
        pro=paginator.page(paginator.num_pages)
    return render(request,'index.html',{'bn':ban,'prodt':prod,'link':links,'pg':pro})

def prodetail(request,c_slug,product_slug):
    try:
        pr=product.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e 
    return render(request,'item.html',{'p':pr})
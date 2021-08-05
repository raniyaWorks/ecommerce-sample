from django.db import models
from django.urls import reverse

# Create your models here.
class banner(models.Model):
    img=models.ImageField(upload_to='banner')
    title1=models.CharField(max_length=250)
    title2=models.CharField(max_length=300)

class categ(models.Model):
    name=models.CharField(max_length=156,unique=True)
    slug=models.SlugField(max_length=156,unique=True)
    img=models.ImageField(upload_to='category')

    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'
    def get_url(self):
        return reverse('hm',args=[self.slug])


    def __str__(self):
        return '{}'.format(self.name)


class product(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    desc=models.TextField()
    img=models.ImageField(upload_to='products')
    category=models.ForeignKey(categ,on_delete=models.CASCADE)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=('name',)
        verbose_name='product'
        verbose_name_plural='products'

    def __str__(self):
        return '{}'.format(self.name)

    def get_url(self):
        return reverse('productitem',args=[self.category.slug,self.slug])

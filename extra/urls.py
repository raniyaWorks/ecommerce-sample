from django.urls import path
from . import views

urlpatterns=[
    path('search',views.search,name='search'),
    path('cart',views.cart_list,name='cart_details'),
    path('add/<int:product_id>/',views.add_cart,name='addcart'),
    path('remove/<int:product_id>/',views.cart_remove,name='cart_remove'),
    path('delete/<int:product_id>/',views.item_remove,name='remove'),
]
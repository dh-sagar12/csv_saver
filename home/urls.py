from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('mypurchases/', MyPurchases.as_view(), name='my_purchases'), 
    path('mycart/', MyCartPage, name='my_cart'), 
    path('postcart/<int:id>', PostCartView, name='post_cart'),
    path('removecart/<int:id>', RemoveCartItem, name='remove_cart'),
]

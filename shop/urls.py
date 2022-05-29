from django.urls import path
from .views import *


urlpatterns = [
    path('', shop, name='shop'),
    path('shop-details/<slug:product_slug>/', product, name='product'),
]
from django.urls import path
from .views import *


urlpatterns = [
    path('', shop, name='shop'),
    path('shop-details/<int:product_id>/', product, name='product'),
]
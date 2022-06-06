from django.urls import path
from .views import *
from cart.views import *

urlpatterns = [
    path('', ShopView.as_view(), name='shop'),
    path('product/<int:id>/', product, name='product'),
]

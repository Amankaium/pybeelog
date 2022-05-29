from django.urls import path
from .views import *


urlpatterns = [
    path('', shop, name='shop'),
    path('product/<int:id>/', product, name='product'),
]
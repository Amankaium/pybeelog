from django.urls import path
from django.views.decorators.cache import cache_page
from .views import *

urlpatterns = [

    path('', cache_page(60)(ShopView.as_view()), name='shop'),
    path('product/<int:id>/', product, name='product'),

]

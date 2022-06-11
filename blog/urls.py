from django.urls import path
from .views import *

urlpatterns = [
    path('', Blog, name='blog'),
    path('post/<int:id>/', Post, name='post'),
]

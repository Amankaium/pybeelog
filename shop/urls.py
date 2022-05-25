from django.urls import path
from .views import *


urlpatterns = [
    path('', ProductHome.as_view(), name='home'),
]
from django.shortcuts import render
from django.views.generic import ListView

from .models import *

class ProductHome(ListView):
    model = Product


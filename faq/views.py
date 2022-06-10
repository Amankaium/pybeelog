from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import FormView

from .forms import FaqFeedbackForm
from .models import *
# Create your views here.


class FaqView(ListView, FormView):
    template_name = 'faq/faq.html'
    success_url = '/faq/'
    model = Faq
    context_object_name = 'faqs'
    form_class = FaqFeedbackForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

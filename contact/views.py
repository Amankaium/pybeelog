from django.views.generic import ListView, CreateView
from django.shortcuts import render, redirect, HttpResponseRedirect

from django.views.generic import FormView
from django.urls import reverse_lazy

from .models import Subscribe, Feedback
from .forms import FeedbackForm, SubscribeForm
from django.http import HttpResponseNotFound


class FeedbackView(FormView, ListView):
    template_name = 'contact/contact.html'
    form_class = FeedbackForm
    success_url = '/contact/'
    model = Feedback
    context_object_name = 'contact'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)



class SubscribeView(CreateView):
    model = Subscribe
    form_class = SubscribeForm
    success_url = '/'
    template_name = 'contact.html'




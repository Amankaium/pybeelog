from django.views.generic import ListView, CreateView
from django.shortcuts import render, redirect, HttpResponseRedirect

# Create your views here.
from django.views.generic import FormView
from django.urls import reverse_lazy

from .models import OurContact, Subscribe
from .forms import FeedbackForm, SubscribeForm
from django.http import HttpResponseNotFound


class FeedbackView(FormView, ListView):
    template_name = 'contact/contact.html'
    form_class = FeedbackForm
    success_url = '/contact/'
    model = OurContact
    context_object_name = 'contact'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def handle_not_found(request, exception):
    return render(request, 'not-found.html')

# def handle_not_found(request, exception):
#    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


class SubscribeView(CreateView):
    model = Subscribe
    form_class = SubscribeForm
    success_url = '/'
    template_name = 'contact.html'


def index(request):
    return render(request, 'index.html')

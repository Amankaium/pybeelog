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



def subscribe(request):
    if request.method == 'POST':
        sub = Subscribe()
        sub.email = request.POST.get('email')
        sub.save()
    return redirect('contact/contact.html')






from cProfile import label
from dataclasses import field
from tkinter import Widget
from django import forms

from .models import Feedback, Subscribe


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('first_name', 'last_name', 'email',
                  'phone', 'title', 'message')

        widgets = {
            'first_name': forms.TextInput(attrs={"class": "form-control"}),
            'last_name': forms.TextInput(attrs={"class": "form-control"}),
            'email': forms.TextInput(attrs={"class": "form-control"}),
            'phone': forms.TextInput(attrs={"class": "form-control"}),
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'message': forms.Textarea(attrs={"class": "form-control"}),
        }


class SubscribeForm(forms.ModelForm):
    '''Форма подписки по email'''
    class Meta:
        model = Subscribe
        fields = ("email", )
        widgets = {
            "email": forms.TextInput(
                attrs={
                    "class": "input-newsletter",
                    "placeholder": "Enter Email Address"
                })
        }
        labels = {
            "email": ''
        }

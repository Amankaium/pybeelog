from random import choices
from django.db import models
from django.forms import CharField, DateTimeField

class Order(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    address = models.CharField(max_length=35)
    phone = models.IntegerField()
    notes = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    pay_method = models.CharField(max_length=5)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ['-data']
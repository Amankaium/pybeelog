from django.shortcuts import render, redirect
from .models import Order

def checkout(request):
    if request.method == 'POST':
        order = Order()
        order.first_name = request.POST.get('first')
        order.last_name = request.POST.get('last')
        order.address = request.POST.get('address')
        order.phone = request.POST.get('phone')
        order.notes = request.POST.get('notes')
        order.pay_method = request.POST.get('radio-group')
        order.save()

    return render(request, 'checkout.html')

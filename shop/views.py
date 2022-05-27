from xml.etree.ElementTree import Comment
from django.shortcuts import render
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import *

def shop(request):
    products = Product.objects.all().order_by('id')
    paginator = Paginator(products, 6)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage: 
        products = paginator.page(paginator.num_pages)
    return render(request, 'shop/shop.html', {'products': products})

# class ShopHome(ListView):
#     model = Product
#     template_name = 'shop/shop.html'



def product(request, product_id):

    product = Product.objects.get(id=product_id)
    # product.update(view_count=product.view_count+1)
    # com = product.comments.filter(product_id=id)

    if request.method == "POST":
        comment = Review()
        comment.product_id = product_id
        comment.author = request.POST.get('author')
        comment.email = request.POST.get('email')
        comment.comment = request.POST.get('comment')
        comment.save()
    return render(request, 'shop/shop-details.html', {'product': product})


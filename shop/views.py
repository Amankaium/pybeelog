from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from .models import *

def shop(request):
    products = Product.objects.all().order_by('id')
    paginator = Paginator(products, 8)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage: 
        products = paginator.page(paginator.num_pages)
    return render(request, 'shop/shop.html', {'products': products})




def product(request, id):
    
    product = Product.objects.get(id=id)
    product.view_count = product.view_count + 1
    product.save()
    com = product.review.filter(post_id=id)
    feature_products = Product.objects.all().order_by('view_count')[:8]
    related_products = Product.objects.all().order_by('view_count')[:4]
    popular_products = Product.objects.all().order_by('view_count')[:3]
    
    if request.method == "POST":
        comment = Review()
        comment.post_id = id
        comment.author = request.POST.get('name')
        comment.email = request.POST.get('email')
        comment.title = request.POST.get('review-title')
        comment.comment = request.POST.get('review-body')
        comment.save()
    return render(request, 'shop/shop-details.html', {'product':product, 'comments': com, 'related_products': related_products, 'feature_products':feature_products, 'popular_products':popular_products})



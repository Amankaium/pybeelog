from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from .models import *

def shop(request):
    products = Product.objects.all().order_by('slug')
    paginator = Paginator(products, 6)
    # paginator = Paginator(products, 6)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage: 
        products = paginator.page(paginator.num_pages)
    return render(request, 'shop/shop.html', {'products': products,})




def product(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    
    # product = Product.objects.get(id=product_id)
    # product.update(view_count=product.view_count+1)
    # com = product.comments.filter(product_slug=slug)

    # if request.method == "POST":
    #     comment = Review()
    #     comment.product_id = id
    #     comment.author = request.POST.get('author')
    #     comment.email = request.POST.get('email')
    #     comment.comment = request.POST.get('comment')
    #     comment.save()
    return render(request, 'shop/shop-details.html', {'product':product})



from django.shortcuts import render
<<<<<<< HEAD
from shop.models import Product
from blog.models import Post
=======
from shop.models import *
>>>>>>> e1558a1a3752e87c3fac38391fdbbcd8fe60f8d4


# from blog.models import *


def homepage(request):
    product = Product.objects.all().order_by('id')
    trending_products = Product.objects.all().order_by('view_count')[:8]
    featured_products = Product.objects.all().order_by('view_count')[:8]
    best_seller_products = Product.objects.all().order_by('view_count')[:6]

    latest_blog = Post.objects.all().order_by('visit_count')[:3]

    
    return render(request, 'core/index.html', {'product': product, 'trending_products': trending_products, \
                                                'featured_products':featured_products, 'best_seller_products': best_seller_products, 'latest_blog': latest_blog})

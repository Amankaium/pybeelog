from django.shortcuts import render

from shop.models import Product
from blog.models import Post


def homepage(request):
    product = Product.objects.all().order_by('id')
    trending_products = Product.objects.all().order_by('view_count')[:8]
    featured_products = Product.objects.all().order_by('view_count')[:8]
    best_seller_products = Product.objects.all().order_by('view_count')[:6]

    latest_blog = Post.objects.all().order_by('visit_count')[:3]

    return render(request, 'core/index.html', {'product': product, 'trending_products': trending_products, \
                                               'featured_products': featured_products,
                                               'best_seller_products': best_seller_products,
                                               'latest_blog': latest_blog})

def terms_conditions(request):
    return render(request, 'core/terms-of-service.html')

def pravicy_policy(request):
    return render(request, 'core/pravicy-policy.html')
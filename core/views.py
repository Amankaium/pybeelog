from django.shortcuts import render
from shop.models import *
#from blog.models import *




def homepage(request):
    product = Product.objects.all().order_by('id')
    trending_products = Product.objects.all().order_by('view_count')[:8]
    featured_products = Product.objects.all().order_by('view_count')[8:]
    best_seller_products = Product.objects.all().order_by('view_count')[:6]
    #latest_blog = Post.objects.all().order_by('visit_count')[:4]
    return render(request, 'core/index.html', {'product': product, 'trending_products': trending_products, \
                                                'featured_products':featured_products, 'best_seller_products': best_seller_products})

# Create your views here.

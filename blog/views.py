from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def Blog(request):
    information = blog.objects.all().order_by('id')
    paginator = Paginator(information)
    page = request.GET.get('page')
    try:
        blog = paginator.page(page)
    except PageNotAnInteger:
        blog = paginator.page(1)
    except EmptyPage: 
        blog = paginator.page(paginator.num_pages)
    return render(request, 'blog/blog-1.html', {'information': information})




def Post(request, id):
    
    details = Post.objects.get(id=id)
    Post.view_count = Post.view_count + 1
    Post.save()
    review = Post.review.filter(post_id=id)
    
    
    if request.method == "POST":
        comment = review()
        comment.post_id = id
        comment.author = request.POST.get('name')
        comment.email = request.POST.get('email')
        comment.website = request.POST.get('website')
        comment.comment = request.POST.get('comment')
        comment.save()
    return render(request, 'blog/blog-details.html', {'details':details})
 
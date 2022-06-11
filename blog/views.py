from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.decorators.csrf import csrf_exempt


def Blog(request):
    information = Post.objects.all().order_by('id')
    paginator = Paginator(information, per_page=10)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage: 
        blog = paginator.page(paginator.num_pages)
    return render(request, 'blog/blog-1.html', {'posts': 'posts'})



@csrf_exempt
def PostView(request, id):
    details = Post.objects.get(id=id)
    details.visits +=1
    details.save()
    comments = details.comments
    popular_posts=Post.objects.order_by('-visits').all()[5:]

    
    if request.method == "POST":
        comment = Comment(
        author=request.POST.get('author'),
        email=request.POST.get('email'),
        comment=request.POST.get('comment')
        )
       
        comment.post = details
        comment.save()
    return render(request, 'blog/blog-details.html', {'details':details, 'popular_posts': popular_posts})
 
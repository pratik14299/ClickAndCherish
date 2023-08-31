# blog/views.py
from django.shortcuts import render, get_object_or_404
from .models import Post,Specification


def Homeview(request): 
    posts = Post.objects.all()
    print(posts) 
    return render(request, 'base.html', {'posts': posts})


def post_list(request):
    posts = Post.objects.all().order_by('-published_date')
    print(posts)
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk) 
    return render(request, 'post_detail.html', {'post': post})


def post_search(request):
    query = request.GET.get('q')
    posts = None

    if query:
        posts = Post.objects.filter(title__icontains=query)

    return render(request, 'post_search.html', {'posts': posts, 'query': query})
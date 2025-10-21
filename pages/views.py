from django.shortcuts import render, get_object_or_404
from .models import *


def index(request, slug=None):
    posts = Post.objects.filter(status=True)
    categories = Catgory.objects.all()
    if slug:
        posts = posts.filter(author__name = slug)
    context = {'posts':posts, 'categories':categories}
    return render(request, 'index.html', context)


def single_post(request,slug):
    post = get_object_or_404(Post, pk=slug)
    context = {'post':post}
    return render(request, 'single-post.html', context)


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def catgory(request, slug=None, pk=None):
    posts = Post.objects.filter(status=True)
    categories = Catgory.objects.all()
    
    if slug:
        posts = posts.filter(author__name = slug)
    if pk:
        posts = posts.filter(catgory__name = pk)
    context = {'posts':posts, 'categories':categories}
    return render(request, 'category.html', context)


def search(request):
    posts = Post.objects.filter(status=True)
    if request.method == 'GET':
        if s := request.GET.get('s'):
            posts = posts.filter(title__icontains=s)
    context = {'posts':posts}
    return render(request, 'index.html', context)
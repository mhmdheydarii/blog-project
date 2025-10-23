from django.shortcuts import render, get_object_or_404
from .models import *


def index(request, author=None, tag_name=None):
    posts = Post.objects.filter(status=True)
    categories = Category.objects.all()
    if author:
        posts = posts.filter(author__name = author)
    if tag_name:
        posts = posts.filter(tag__name = tag_name)
    context = {'posts':posts, 'categories':categories}
    return render(request, 'index.html', context)


def single_post(request,pk):
    post = get_object_or_404(Post, pk=pk)
    context = {'post':post}
    return render(request, 'single-post.html', context)


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def category(request, author=None, category=None):
    posts = Post.objects.filter(status=True)
    categories = Category.objects.all()
    
    if author:
        posts = posts.filter(author__name = author)
    if category:
        posts = posts.filter(category__name = category)
    context = {'posts':posts, 'categories':categories}
    return render(request, 'category.html', context)


def search(request):
    posts = Post.objects.filter(status=True)
    if request.method == 'GET':
        if s := request.GET.get('s'):
            posts = posts.filter(title__icontains=s)
    context = {'posts':posts}
    return render(request, 'index.html', context)
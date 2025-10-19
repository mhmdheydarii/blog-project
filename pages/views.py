from django.shortcuts import render, get_object_or_404
from .models import *


def index(request):
    posts = Post.objects.filter(status=True)
    context = {'posts':posts}
    return render(request, 'index.html', context)


def single_post(request,slug):
    posts = get_object_or_404(Post, pk=slug)
    context = {'posts':posts}
    return render(request, 'single-post.html', context)


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def catgory(request):
    return render(request, 'catgory.html')


def search(request):
    posts = Post.objects.filter(status=True)
    if request.method == 'GET':
        if s := request.GET.get('s'):
            posts = posts.filter(title__contains=s)
    context = {'posts':posts}
    return render(request, 'index.html', context)
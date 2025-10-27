from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .forms import *
from django.contrib import messages

def index(request, author=None, tag_name=None):
    posts = Post.objects.filter(status=True)
    categories = Category.objects.all()
    if author:
        posts = posts.filter(author__name = author)
    if tag_name:
        posts = posts.filter(tag__name = tag_name)
    
    posts = Paginator(posts, 3)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    context = {'posts':posts, 'categories':categories}
    return render(request, 'index.html', context)


def single_post(request,pk):
    post = get_object_or_404(Post, pk=pk)

    next_post = Post.objects.filter(status=True, id__gt=post.id).order_by('id').first()
    prev_post = Post.objects.filter(status=True, id__lt=post.id).order_by('-id').first()
    context = {'post':post, 'next_post':next_post ,'prev_post':prev_post}
    return render(request, 'single-post.html', context)


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
        else:
            messages.error(request, 'Please fill in all required fields before sending.')

    form = ContactForm()
    context = {'form':form}
    return render(request, 'contact.html', context)


def category(request, author=None, category=None):
    posts = Post.objects.filter(status=True)
    categories = Category.objects.all()
    
    if author:
        posts = posts.filter(author__name = author)
    if category:
        posts = posts.filter(category__name = category)

    posts = Paginator(posts, 3)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    context = {'posts':posts, 'categories':categories}
    return render(request, 'category.html', context)


def search(request):
    posts = Post.objects.filter(status=True)
    if request.method == 'GET':
        if s := request.GET.get('s'):
            posts = posts.filter(title__icontains=s)
    context = {'posts':posts}
    return render(request, 'index.html', context)
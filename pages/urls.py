from django.urls import path
from .views import *

app_name = 'pages'

urlpatterns = [
    path('', index, name = 'index'),
    path('post/<int:pk>', single_post, name = 'single_post'),
    path('about/' , about, name = 'about'),
    path('contact/', contact, name = 'contact'),
    path('category/<str:category>/', category, name = 'category'),
    path('search/', search, name = 'search'),
    path('author/<str:author>/', index, name = 'author'),
    path('tag/<str:tag_name>/', index, name = 'tag'),
]
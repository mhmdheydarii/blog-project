from django.urls import path
from .views import *

app_name = 'pages'

urlpatterns = [
    path('', index, name = 'index'),
    path('post/<int:slug>', single_post, name = 'single_post'),
    path('about/' , about, name = 'about'),
    path('contact/', contact, name = 'contact'),
    path('catgory/', catgory, name = 'catgory'),
    path('search/', search, name = 'search'),
    path('author/<str:slug>/', index, name = 'author'),
]
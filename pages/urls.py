from django.urls import path
from .views import *

app_name = 'pages'

urlpatterns = [
    path('', index, name = 'index'),
    path('post/<str:slug>', single_post, name = 'single_post'),
    path('about/' , about, name = 'about'),
    path('contact/', contact, name = 'contact'),
    path('catgory/', catgory, name = 'catgory'),
]
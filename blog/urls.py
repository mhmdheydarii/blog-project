from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('single', single_blog, name = 'single'),
]
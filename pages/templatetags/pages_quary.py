from django import template
from pages.models import *

register = template.Library()

@register.inclusion_tag("lates-post.html")
def lates_post():
    posts = Post.objects.filter(status=True)[:1]
    return posts

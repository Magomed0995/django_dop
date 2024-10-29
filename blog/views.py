from django.shortcuts import render
from django.utils import timezone

from .models import MyPost 

def get_posts(request):
    posts  = MyPost.objects.exclude(is_published=False).order_by('-created_date')
    return render(request, 'blog/posts.html', {'posts': posts})

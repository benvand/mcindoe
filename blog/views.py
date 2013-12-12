# Create your views here.
# Create your views here.
from django.shortcuts import render
from django.contrib.sites.models import get_current_site
from models import BlogOptions, Post
from django.contrib.auth.models import User

def blog(request):
    site = get_current_site(request)
    blog = BlogOptions.objects.get(site=site)
    context = {'global_site': site, "blog": blog, "posts": Post.objects.all }
    return render(request, 'blog/blog.html', context)
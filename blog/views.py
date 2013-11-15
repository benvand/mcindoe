# Create your views here.
# Create your views here.
from django.shortcuts import render
from django.contrib.sites.models import get_current_site
from models import BlogOptions

def blog(request):
    site = get_current_site(request)
    blog = BlogOptions.objects.get(site=site)
    context = {'global_site': site, "blog": blog}
    return render(request, 'blog/blog.html', context)
# Create your views here.
from django.shortcuts import render
from django.contrib.sites.models import get_current_site
from models import AboutOptions


def about(request):
    site = get_current_site(request)
    about = AboutOptions.objects.get(site=site)
    context = {'global_site': site, "about": about}
    return render(request, 'about/about.html', context)

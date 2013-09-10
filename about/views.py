# Create your views here.
from django.shortcuts import render
from django.contrib.sites.models import get_current_site
from models import AboutOptions

def about(request):
   Site = get_current_site(request)
   about = AboutOptions.objects.get(site=Site)
   context = {'global_site':Site, "about" : about }
   return render(request, 'about/about.html', context)
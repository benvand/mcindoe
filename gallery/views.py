from django.shortcuts import render
from django.contrib.sites.models import get_current_site
from models import GalleryOptions

def gallery(request):
   Site = get_current_site(request)
   gallery = GalleryOptions.objects.get(site=Site)
   context = {'global_site':Site, "gallery" : gallery }
   return render(request, 'gallery/gallery.html', context)
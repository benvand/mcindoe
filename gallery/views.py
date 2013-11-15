from django.shortcuts import render
from django.contrib.sites.models import get_current_site
from models import GalleryOptions, Picture

def gallery(request):
   site = get_current_site(request)
   gallery = GalleryOptions.objects.get(site=site)
   pictures = Picture.objects.all()
   #pictures= [i.picture.url.strip('static/gallery') for i in  pictures]
   context = {'global_site':site, "gallery" : gallery, 'pictures': pictures}
   return render(request, 'gallery/gallery.html', context)
from django.conf.urls import patterns, include, url

from django.shortcuts import render
from django.contrib.sites.models import get_current_site

#App Specific

def fastprod(request):
   Site = get_current_site(request)
   context = {'global_site':Site, 'appname':'gallery'}
   return render(request, 'fastprod.html', context)

urlpatterns = patterns('', url( '^$', fastprod, name='gallery' ))
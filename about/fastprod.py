from django.conf.urls import patterns, include, url

from django.shortcuts import render
from django.contrib.sites.models import get_current_site

#App Specific
from django.contrib.contenttypes.models import ContentType
def fastprod(request):
   Site = get_current_site(request)
   context = {'global_site':Site, 'appname':'about'}
   return render(request, 'fastprod.html', context)

urlpatterns = patterns('', url( '^$', fastprod, name='about' ))
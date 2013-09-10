from django.conf.urls import patterns, include, url
import gallery.views

#App Specific
urlpatterns = patterns('', url( '^$', gallery.views.gallery, name='gallery' ))
from django.conf.urls import patterns, include, url
import about.views

#App Specific
urlpatterns = patterns('', url( '^$', about.views.about, name='about' ))

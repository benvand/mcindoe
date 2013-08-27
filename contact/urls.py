from django.conf.urls import patterns, include, url
from contact import views

#App Specific
urlpatterns = patterns('', url( '^$', views.comingSoon, name='ComingSoon' ))

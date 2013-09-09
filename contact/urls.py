from django.conf.urls import patterns, include, url
import contact.views

#App Specific
urlpatterns = patterns('', url( '^$', contact.views.contact, name='contact' ))

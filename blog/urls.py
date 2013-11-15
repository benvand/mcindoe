from django.conf.urls import patterns, include, url
import blog.views

#App Specific
urlpatterns = patterns('', url( '^$', blog.views.blog, name='blog' ))

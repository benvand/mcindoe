from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import views

#Admin


admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mcindoe.views.home', name='home'),
    # url(r'^mcindoe/', include('mcindoe.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:

)


#admin

urlpatterns += patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^maddyonly/', include(admin.site.urls)),)

#Stuff to serve static admin content
urlpatterns += patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),)
urlpatterns += staticfiles_urlpatterns()


#comingsoon
urlpatterns += patterns('', url( '^$', views.comingSoon, name='ComingSoon' ))

#Apps
if settings.DEV:
    urlpatterns += patterns('', url('^contact/',include('contact.urls')),)
    # urlpatterns += patterns('', url('^blog/',include('blog.urls')),)
    # urlpatterns += patterns('', url('^gallery/',include('gallery.urls')),)
    # urlpatterns += patterns('', url('^about/',include('about.urls')),)

#Error Pages
handler500 = views.fiveHundred
handler404 = views.fourHundred

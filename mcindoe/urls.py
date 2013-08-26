from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
# Apps
from contact import views as contactviews
from django.conf import settings



from django.contrib.staticfiles.urls import staticfiles_urlpatterns

#Admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mcindoe.views.home', name='home'),
    # url(r'^mcindoe/', include('mcindoe.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

#Stuff to serve static admin content
urlpatterns += patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)

urlpatterns += staticfiles_urlpatterns()




#Apps
urlpatterns += patterns('', url( '', include('contact.urls')))

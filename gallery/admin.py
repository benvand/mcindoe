from django.contrib import admin
from gallery.models import Picture, Comment, GalleryOptions

admin.site.register(Picture)
admin.site.register(Comment)
admin.site.register(GalleryOptions)

from django.contrib import admin
from gallery.models import Picture, Comment, GalleryOptions
from app_config import config

admin.site.register(Picture)
admin.site.register(GalleryOptions)
if config.comments:
    admin.site.register(Comment)

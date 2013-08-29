from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site

User = get_user_model()


class Picture(models.Model):
    title =             models.CharField(max_length=255, blank=True)
    picture =           models.ImageField(upload_to='gallery/static/pics')
    description =       models.TextField(blank=True) 
    created =           models.TimeField(auto_now_add=True)
    modified =          models.TimeField(auto_now=True)
    userid =            models.ForeignKey(User, related_name='usergallerypicture')

    class Meta():
        ordering = ('created',)
        get_latest_by = ('created',)
        verbose_name = 'Gallery Picture'
        verbose_name_plural = 'Gallery Pictures'

class Comment(models.Model):
    content =           models.TextField() 
    created =           models.TimeField(auto_now_add=True)
    modified =          models.TimeField(auto_now=True)
    userid =            models.ForeignKey(User, related_name='usergallerycomment')
    postid =            models.ForeignKey('Picture')

    class Meta():
        ordering = ('modified',)
        get_latest_by = ('created',)
        verbose_name = 'Gallery Comment'
        verbose_name_plural = 'Gallery Comments'


class GalleryOptions(models.Model):
    site = models.OneToOneField(Site)
    backgroundImage = models.ImageField(upload_to='static', blank=True)

    class Meta:
        verbose_name = 'Gallery Page Options'
        verbose_name_plural = 'Gallery Page Options'

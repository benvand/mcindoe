from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
from stdimage import StdImageField

User = get_user_model()


class Picture(models.Model):
    title =             models.CharField(max_length=255, blank=True)
    picture =           StdImageField(upload_to='gallery/GalleryImages', blank=True, size=(640, 480), thumbnail_size=(100, 100))
    description =       models.TextField(blank=True) 
    created =           models.TimeField(auto_now_add=True)
    modified =          models.TimeField(auto_now=True)
    userid =            models.ForeignKey(User, related_name='usergallerypicture')

    def __unicode__(self):
        return self.title

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

    def __unicode__(self):
        return User.objects.get(id=self.userid).username + ':' + self.content[:50]

    class Meta():
        ordering = ('modified',)
        get_latest_by = ('created',)
        verbose_name = 'Gallery Comment'
        verbose_name_plural = 'Gallery Comments'


class GalleryOptions(models.Model):
    site = models.OneToOneField(Site)
    backgroundImage = models.ImageField(upload_to='gallery', blank=True)

    def __unicode__(self):
        return self.site.name.capitalize() + " Gallery Page Options"
    class Meta:
        verbose_name = 'Gallery Page Options'
        verbose_name_plural = 'Gallery Page Options'

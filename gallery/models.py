from django.db import models
from django.contrib.auth import get_user_model
#User class is:
User = get_user_model()
# Create your models here.

class Picture(models.Model):
    title =             models.CharField(max_length=255)
    picture =           models.ImageField(upload_to='gallery/static/pics')
    description =       models.TextField() 
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
        verbose_name = 'Gallery Pic Comment'
        verbose_name_plural = 'Gallery Pic Comments'

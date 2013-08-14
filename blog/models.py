from django.db import models
from django.contrib.auth import get_user_model
#User class is:
User = get_user_model()
# Create your models here.

class Post(models.Model):
    title =             models.CharField(max_length=255)
    content =           models.TextField() 
    picture =           models.ImageField(upload_to='blog/static/post_pics')
    created =           models.TimeField(auto_now_add=True)
    modified =          models.TimeField(auto_now=True)
    userid =            models.ForeignKey(User, related_name='userblogpost')

    class Meta():
        ordering = ('created',)
        get_latest_by = ('created',)
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'

class Comment(models.Model):
    content =           models.TextField() 
    created =           models.TimeField(auto_now_add=True)
    modified =          models.TimeField(auto_now=True)
    userid =            models.ForeignKey(User)
    postid =            models.ForeignKey('Post')

    class Meta():
        ordering = ('created',)
        get_latest_by = ('created',)
        verbose_name = 'Blog Comment'
        verbose_name_plural = 'Blog Comments'

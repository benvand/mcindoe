from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
#User class is:
User = get_user_model()
# Create your models here.

class Post(models.Model):
    title =             models.CharField(max_length=255)
    content =           models.TextField()
    created =           models.DateTimeField(auto_now_add=True)
    modified =          models.DateTimeField(auto_now=True)
    userid =            models.ForeignKey(User, related_name='userblogpost')
    PostPicture = None

    def __unicode__(self):
        return self.title

    class Meta():
        ordering = ('created',)
        get_latest_by = ('created',)
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'

class Comment(models.Model):
    content =           models.TextField() 
    created =           models.TimeField(auto_now_add=True)
    modified =          models.TimeField(auto_now=True)
    userid =            models.ForeignKey(User, related_name='userblogcomment')
    postid =            models.ForeignKey('Post')

    def __unicode__(self):
        return self.userid + ': ' + self.content[:20]

    class Meta():
        ordering = ('created',)
        get_latest_by = ('created',)
        verbose_name = 'Blog Comment'
        verbose_name_plural = 'Blog Comments'

class PostPicture(models.Model):
    picture =           models.ImageField(upload_to='blog/post_pics', blank=True)
    postid =            models.ForeignKey('Post')



class BlogOptions(models.Model):
    site = models.OneToOneField(Site)
    title = models.CharField(max_length=200,blank=True)
    intro = models.TextField(max_length=1000,blank=True)
    backgroundImage = models.ImageField(upload_to='blog/', blank=True)

    def __unicode__(self):
        return self.site.name.capitalize() + " Blog Page Options"

    class Meta:
        verbose_name = 'Blog Page Options'
        verbose_name_plural = 'Blog Page Options'

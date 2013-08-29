from django.db import models
#from justdifferentsites.models import Site
from django.contrib.sites.models import Site
# Create your models here.


class ContactOptions(models.Model):
    site = models.OneToOneField(Site)
    contactmessage = models.TextField(max_length=1000,blank=True)
    addressline1 = models.CharField(max_length=200,blank=True)
    addressline2 = models.CharField(max_length=200,blank=True)
    county = models.CharField(max_length=200,blank=True)
    city = models.CharField(max_length=200,blank=True)
    postcode = models.CharField(max_length=200,blank=True)
    mapurl = models.URLField(blank=True)
    contactsignoff = models.TextField(max_length=1000, blank=True)
    backgroundImage = models.ImageField(upload_to='static', blank=True)

    class Meta:
        verbose_name = 'Contact Page Option'
        verbose_name_plural = 'Contact Page Options'

from django.db import models
from django.contrib import sites


newVariables = [
    ('twitter', models.URLField(blank=True)),
    ('tumblr', models.URLField(blank=True)),
    ( 'backgroundImage', models.ImageField(upload_to='static', blank=True))
]

for i in newVariables:
    sites.models.Site.add_to_class(*i)

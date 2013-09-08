from django.db import models
from django.contrib import sites



newVariables = [
    ('twitter', models.URLField(blank=True)),
    ('tumblr', models.URLField(blank=True)),
    ('email', models.EmailField(blank=True)),
    ('backgroundImage1', models.ImageField(upload_to='static', blank=True)),
    ('backgroundImage2', models.ImageField(upload_to='static', blank=True)),
    ('favicon', models.ImageField(upload_to='static', blank=True)),
]

for i in newVariables:
    sites.models.Site.add_to_class(*i)

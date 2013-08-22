from django.contrib import admin
from blog.models import Post, Comment, BlogOptions

admin.site.register(BlogOptions)
admin.site.register(Post)
admin.site.register(Comment)

from django.contrib import admin
from blog.models import Post, Comment, BlogOptions, PostPicture

class PostPictureInline(admin.TabularInline):
    model = PostPicture
    # readonly_fields = ('picture',)
    fields = ['picture',]


class PostAdmin(admin.ModelAdmin):
    inlines = [PostPictureInline,]


admin.site.register(Post, PostAdmin)
admin.site.register(BlogOptions)
admin.site.register(Comment)
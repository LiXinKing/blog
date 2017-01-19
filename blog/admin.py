from django.contrib import admin
from blog.models import Post
from blog.models import BlogPostAdmin

#admin.site.register(Post, BlogPostAdmin)
admin.site.register(Post)

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import admin

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length = 250)
    slug = models.SlugField(max_length = 250, unique_for_date = 'publish')
    author = models.ForeignKey(User, related_name = 'blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default = timezone.now)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    status = models.CharField(max_length = 10,
    choices = STATUS_CHOICES, default = 'draft')

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return self.title

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')


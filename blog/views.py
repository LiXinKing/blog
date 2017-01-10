from django.shortcuts import render
from blog.models import Post
from django.template import loader, Context
from django.http import HttpResponse
# Create your views here.

def archive(request):
    posts = Post.objects.all()
    t = loader.get_template("post.html")
    c = Context({'posts' : posts})
    return HttpResponse(t.render(c))

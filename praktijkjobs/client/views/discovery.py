from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from ..models import Post

@login_required
def discovery(request):
    template = "portal/discovery.html"
    posts = Post.objects.all() 
    context = {
        "posts": posts,
    }
    return render(request, template, context)

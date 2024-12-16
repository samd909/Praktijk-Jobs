from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from ..models import Post

@login_required
def dashboard(request):
    template = "portal/dashboard.html"
    posts = Post.objects.all() 
    context = {
        "posts": posts,
    }
    return render(request, template, context)

@login_required
def create_post(request):
    user = request.user
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        deadline = request.POST.get('deadline')   
        budget = request.POST.get('budget')
        location = request.POST.get('location')  



        if title and description:
            new_post = Post.objects.create(
                author=user,
                title=title,
                description=description,
                deadline = deadline,
                budget = budget,
                location = location, 
            )
            new_post.save()

            return redirect('dashboard')
        else:
            return redirect('dashboard')


    return redirect('dashboard')


@login_required
def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if post.author != request.user:
        return redirect('dashboard')  

    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')

        if title and description:
            post.title = title
            post.description = description
            post.save()  

            return redirect('dashboard')  
    return redirect('dashboard')

@login_required
def update_status(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        new_status = request.POST.get('status')
        post.status = new_status
        post.save()

        return redirect('dashboard')  
    return redirect('dashboard')

def view_post(request, id):
    template = 'portal/view.html'
    post = get_object_or_404(Post, id=id)
    context = {
        "post": post
    }
    return render(request, template, context)

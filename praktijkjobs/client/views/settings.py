from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def settings(request):
    template = "portal/settings.html"
    context = {
        
    }
    return render(request, template, context)
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    template = "portal/dashboard.html"
    context = {
        
    }
    return render(request, template, context)
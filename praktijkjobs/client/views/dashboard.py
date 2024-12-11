from django.shortcuts import render, redirect

def dashboard(request):
    template = "portal/dashboard.html"
    context = {
        
    }
    return render(request, template, context)
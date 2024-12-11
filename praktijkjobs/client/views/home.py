from django.shortcuts import render, redirect

def home(request):
    template = "home.html"
    context = {

    }
    return render(request, template, context)
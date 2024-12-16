from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.core.files.storage import default_storage

from ..models import Profile

def setup(request):
    if request.user.profile.permission != 1:
        return redirect('settings')        
    template = 'portal/setup.html'
    context = {

    }
    return render(request, template, context)

def set_role(request):
    if request.method == 'POST':
        user = request.user
        profile = user.profile

        role = request.POST.get('choice')

        if role == 'zoeker':  
            profile.permission = 2  
        elif role == 'aanbieder':  
            profile.permission = 3  
        else:
            return HttpResponse("Invalid role", status=400)

        profile.save()

        return redirect('setup')  

    return HttpResponse("Invalid request method", status=405)
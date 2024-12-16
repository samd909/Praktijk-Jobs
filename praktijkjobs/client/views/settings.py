from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.core.files.storage import default_storage

from ..models import Profile



@login_required
def settings(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    bioData = profile.bio

    template = "portal/settings.html"
    context = {
        'bioData': bioData
        
    }
    return render(request, template, context)

@login_required
def update_bio(request):
    if request.method == "POST":
        user = request.user
        try:
            profile = user.profile
            bio = request.POST.get('bio')
            birth_date = request.POST.get('birth_date')

            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')

            pc = request.POST.get('pc')
            city = request.POST.get('city')
            street = request.POST.get('street')

            if first_name is not None:
                user.first_name  = first_name
                user.last_name = last_name
                user.save()
                
            if bio is not None:
                profile.pc = pc
                profile.street = street
                profile.city = city
                profile.bio = bio
                profile.birth_date = birth_date
                profile.save() 

                return redirect('settings')
            else:
                return redirect({'status': 'error', 'message': 'No bio provided.'}, status=400)
        
        except Profile.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Profile does not exist.'}, status=404)
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=405)


@login_required
def upload_profile_picture(request):
    if request.method == "POST" and request.FILES.get('profile_picture'):
        try:
            profile = request.user.profile
            profile_picture = request.FILES['profile_picture']

            filename = f"profile_pictures/user_{request.user.id}_{profile_picture.name}"
            file_path = default_storage.save(filename, profile_picture)

            profile.profile_picture = file_path
            profile.save()

            return redirect('settings')
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

    return JsonResponse({'status': 'error', 'message': 'No file uploaded or invalid request method.'}, status=400)  

@login_required
def update_aanbieder(request):
    if request.method == "POST":
        user = request.user
        try:
            profile = user.profile
            kvk = request.POST.get('kvk')
                
            if kvk is not None:
                profile.kvk = kvk
     
                profile.save() 

                return redirect('settings')
            else:
                return redirect({'status': 'error', 'message': 'No bio provided.'}, status=400)
        
        except Profile.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Profile does not exist.'}, status=404)
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=405)

from django.urls import path
from django.contrib.auth import views as auth_views
from .views.auth import *
from .views.home import *
from .views.dashboard import *
from .views.settings import *

urlpatterns = [
    path('', dashboard, name='home'),    

    path('dashboard/', dashboard, name="dashboard"),
    path('settings/', settings, name="settings"),

    path('update_bio/', update_bio, name='update_bio' ),
    path('upload_profile_picture/', upload_profile_picture, name='upload_profile_picture'),


    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
]

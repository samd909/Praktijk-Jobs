from django.urls import path
from django.contrib.auth import views as auth_views
from .views.auth import *
from .views.home import *
from .views.dashboard import *
from .views.settings import *
from .views.setup import *


urlpatterns = [
    path('', dashboard, name='home'),    

    path('dashboard/', dashboard, name="dashboard"),
    path('settings/', settings, name="settings"),
    path('setup/', setup, name="setup"),

    path('dashboard/view/<int:id>/', view_post, name='view_post'),

    path('dashboard/status/<int:post_id>/', update_status, name='update_status'),
    path('dashboard/edit/<int:post_id>/', update_post, name='update_post'),
    path('create_post/', create_post, name="create_post"),
    path('set_role', set_role, name="set_role"),
    path('update_bio/', update_bio, name='update_bio' ),
    path('update_aanbieder/', update_aanbieder, name='update_aanbieder' ),

    path('upload_profile_picture/', upload_profile_picture, name='upload_profile_picture'),


    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
]

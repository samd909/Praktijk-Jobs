
from django.urls import path
from django.contrib.auth import views as auth_views
from .views.auth import *
from .views.home import *
from .views.dashboard import *

urlpatterns = [
    path('', home, name='home'),    

    path('dashboard/', dashboard, name="dashboard"),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
]

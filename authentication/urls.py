from django.urls import path, include
from django.contrib.auth.views import *
from .views import *
from django.contrib.auth import views 

urlpatterns = [
    path('logout/',logout_person,name='logout_user'),
    path('login/',login_user,name='login_user'),
    path('sign-up/',register,name='signup'),
    path('reset/password/',views.PasswordResetView.as_view(template_name='password_reset.html'))
]
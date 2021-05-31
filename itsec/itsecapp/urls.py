from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import path, include, reverse_lazy
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import reverse
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home_view,name='home'),
    path('home',views.home_view,name='home'),
    path('mylogin',views.login_view,name='my_login'),
    path('mylogout',views.logout_view,name='my_logout'),
    path('login', auth_views.LoginView.as_view(),name='login'),
    path('logout', auth_views.LogoutView.as_view(),name='logout'),
]
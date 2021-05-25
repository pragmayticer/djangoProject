from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import path, include, reverse_lazy
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import reverse
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/home',views.home_view,name='home'),
    path('login', auth_views.LoginView.as_view(),name='login'),
    path('logout', auth_views.LogoutView.as_view(),name='logout'),
]
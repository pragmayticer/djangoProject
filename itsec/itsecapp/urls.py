from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import reverse
from . import views

urlpatterns = [
    path('',views.home_view),
    path('login',views.login_view),
    path('read',views.read_card),
    # url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'},
    #     name='mysite_login'),
    # url(r'^logout/$', 'django.contrib.auth.views.logout',
    #     {'next_page': reverse_lazy('marcador_bookmark_list')}, name='mysite_logout'),
]
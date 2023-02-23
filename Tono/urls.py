"""Tono URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views
from django.urls import path 
from userprofile.views import signup, login
from item.views import newnote, notedetail, deletenote
from room.views import new_room, all_room, roomdetail, join_room
from core.views import index, base, notes
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('index/', index, name='index'),
    path('base/', base, name='base'),
    path('notes/',notes,name='notes'),
    path('sign-up/', signup, name='signup'),
    path('log-in/', views.LoginView.as_view(template_name='userprofile/login.html'), name='login'),
    path('log-out/',views.LogoutView.as_view(), name='logout'),
    #url structure
    path('newnote/',newnote,name='newnote'),
    path('<int:pk>/', notedetail, name='notedetail'),
    path('<int:pk>/delete/', deletenote, name='deletenote'),

    path('joinroom', join_room, name='joinroom'),
    path('newroom', new_room, name='newroom'),
    path('allroom', all_room, name='roomlist'),
    path('room/<int:pk>/', roomdetail, name='roomdetail'),
]

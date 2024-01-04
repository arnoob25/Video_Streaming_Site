"""
URL configuration for Video_Streaming_Site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from . import views
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),

    # home page
    
    path('home/', views.DisplayVideoList.as_view(), name = 'home'),
    
    # upload functionality

    path('upload/', views.UploadVideo.as_view(), name = 'upload'),

    # connecting apps

    path('stream/', include('video_streaming.urls')),


    # user registration routes

    path('accounts/signup/', views.CreateUser.as_view(), name='signup'),
    path('accounts/login/', LoginView.as_view(template_name='registration.html'), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),

    # redirecting users to proper routes

    path('', views.redirectToHome),
]




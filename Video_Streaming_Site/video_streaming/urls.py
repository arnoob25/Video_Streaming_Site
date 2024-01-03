from . import views
from django.urls import path


app_name = 'video_streaming'

urlpatterns = [
    path('video/', views.streamVideo, name='stream'),
]
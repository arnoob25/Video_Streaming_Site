from . import views
from django.urls import path


app_name = 'video_streaming'

urlpatterns = [
    path('<slug:slug>/', views.StreamVideo.as_view(), name='stream'),
]
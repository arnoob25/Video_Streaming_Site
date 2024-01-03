from . import models
from django.shortcuts import render

# Create your views here.

def streamVideo(request):
    data = models.Video.objects.get(pk=1)
    return render(request, 'stream.html', context={'video': data})
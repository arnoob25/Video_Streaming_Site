from . import models
from django.shortcuts import render

# Create your views here.

def streamVideo(request, slug):
    data = models.Video.objects.get(slug = slug)
    return render(request, 'stream.html', context={'video': data})
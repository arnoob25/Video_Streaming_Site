from . import models
from . import forms
from django.shortcuts import render, redirect

# helper functions for streamVideo()
def saveUserComment(request, video, form):
    if form.is_valid():
        comment = form.save(commit = False)
        comment.author = request.user
        comment.video = video
        comment.save()
        return redirect('video_streaming:stream', slug = video.slug)
    
def getUserComments(video):
    return models.Comment.objects.filter(video = video).order_by('-created_at')

# Create your views here.
    
def streamVideo(request, slug):
    print('streamVideo - is called')
    video = models.Video.objects.get(slug = slug)
    form = forms.CommentForm(request.POST or None)
    comments = getUserComments(video)

    context = {
        'video': video,
        'form': form,
        'comments': comments,
    }

    # saving logged in users' comments and reloading the page
    if request.user.is_authenticated and request.method == 'POST':
        return saveUserComment(request, video, form)


    return render(request, 'stream.html', context = context)
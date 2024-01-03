from typing import Any
from django.db.models.query import QuerySet
from video_streaming import models
from django.urls import reverse_lazy 
from django.contrib.auth import get_user_model
from django.views.generic import CreateView, ListView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, HttpResponseRedirect

def redirectToHome(request):
    return HttpResponseRedirect(
        reverse_lazy('home')
    )

class CreateUser(CreateView):
    model = get_user_model()
    form_class = UserCreationForm
    template_name = 'registration.html'
    success_url = reverse_lazy('login')

class DisplayVideoList(ListView):
    model = models.Video
    template_name = 'home.html'
    context_object_name = 'videos'

    # filtering the queryset allows the search functionality
    def get_queryset(self):  # sourcery skip: use-named-expression
        queryset = super().get_queryset()
        query= self.request.GET.get('searchFilter')
        
        if query:
            queryset = queryset.filter(title__icontains=query)
        
        return queryset


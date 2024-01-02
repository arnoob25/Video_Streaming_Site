from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy 
from django.views.generic import CreateView
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

def redirectToHome(request):
    return HttpResponseRedirect(
        reverse_lazy('home')
    )

def displayHome(request):
    return render(request, 'home.html')

class CreateUser(CreateView):
    model = get_user_model()
    form_class = UserCreationForm
    template_name = 'registration.html'
    success_url = reverse_lazy('login')


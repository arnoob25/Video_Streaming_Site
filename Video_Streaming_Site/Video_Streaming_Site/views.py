from django.shortcuts import render, HttpResponse

def displayIndex(request):
    return HttpResponse('This is the index page')


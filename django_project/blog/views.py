# default import when creating an app 
from django.shortcuts import render

# import HttpResponse
from django.http import HttpResponse


def Home(request):
    return HttpResponse('<h1>Blog Home</h1>')

def About(request):
    return HttpResponse('<h1>Blog About</h1>')
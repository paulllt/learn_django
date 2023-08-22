'''This file is manually created and copied from urls.py under django_project'''

from django.urls import path

# import views from views.py under blog app. "." means the current directory.
from . import views 


urlpatterns = [
    path('', views.Home, name='blog-home'),
    path('about/', views.About, name='blog-home'),
]
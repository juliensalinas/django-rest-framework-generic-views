"""
django_project URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('how_to_app.urls')),
]

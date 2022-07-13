"""URL Configuration
"""
from django.urls import path
from . import views

urlpatterns = [
    # TODO: use urls in products as basis
    path('', views.all_workouts, name='workouts'),
]

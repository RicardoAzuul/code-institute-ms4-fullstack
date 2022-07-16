"""URL Configuration
"""
from django.urls import path
from . import views

urlpatterns = [
    # TODO: use urls in products as basis
    path('', views.all_workouts, name='workouts'),
    path('<int:workout_id>/', views.workout_detail, name='workout_detail'),
]

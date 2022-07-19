"""URL Configuration
"""
from django.urls import path
from . import views

urlpatterns = [
    # TODO: use urls in products as basis
    path('', views.all_workouts, name='workouts'),
    path('<int:workout_id>/', views.workout_detail, name='workout_detail'),
    path('add/', views.add_workout, name='add_workout'),    
    path('edit/<int:workout_id>/', views.edit_workout, name='edit_workout'),
    path('delete/<int:workout_id>/',
         views.delete_workout, name='delete_workout'),
]

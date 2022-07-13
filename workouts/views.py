from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def all_workouts(request):
    """ A view to show all workouts, including sorting and search queries """
    # TODO: use views.py in products as a basis

    return render(request, 'workouts/workouts.html')

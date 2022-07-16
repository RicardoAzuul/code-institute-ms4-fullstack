from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required

from workouts.models import Workout


# Create your views here.
@login_required
def all_workouts(request):
    """ A view to show all workouts, including sorting and search queries """
    # TODO: use views.py in products as a basis

    workouts = Workout.objects.all()
    # set to None in case of no search term or category
    query = None
    categories = None
    sort = None
    direction = None

    context = {
        'workouts': workouts,
        'search_term': query,
        'selected_categories': categories,
    }

    return render(request, 'workouts/workouts.html', context)


def workout_detail(request, workout_id):
    """ A view to show workout details """

    workout = get_object_or_404(Workout, pk=workout_id)

    context = {
        'workout': workout,
    }

    return render(request, 'workouts/workout_detail.html', context)

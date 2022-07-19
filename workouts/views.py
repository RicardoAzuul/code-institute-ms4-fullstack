from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required

from workouts.models import BodyPart, Equipment, Target, Workout
from .forms import WorkoutForm


# Create your views here.
@login_required
def all_workouts(request):
    """ A view to show all workouts, including sorting and search queries """
    # TODO: use views.py in products as a basis

    workouts = Workout.objects.all()
    # set to None in case of no search term or category
    body_parts = None
    equipment = None
    targets = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                workouts = workouts.annotate(lower_name=Lower('name'))
            if sortkey == 'body_part':
                sortkey = 'body_part__name'
            if sortkey == 'equipment':
                sortkey = 'equipment__name'
            if sortkey == 'target':
                sortkey = 'target__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            workouts = workouts.order_by(sortkey)

        if 'body_part' in request.GET:
            print("body part in request")
            body_parts = request.GET['body_part'].split(',')
            workouts = workouts.filter(body_part__name__in=body_parts)
            body_parts = BodyPart.objects.filter(name__in=body_parts)
        
        if 'equipment' in request.GET: 
            equipment = request.GET['equipment'].split(',')
            workouts = workouts.filter(equipment__name__in=equipment)
            equipment = Equipment.objects.filter(name__in=equipment)
        
        if 'target' in request.GET:
            targets = request.GET['target'].split(',')
            workouts = workouts.filter(target__name__in=targets)
            targets = Target.objects.filter(name__in=targets)

    selected_sorting = f'{sort}_{direction}'

    context = {
        'workouts': workouts,
        'selected_body_parts': body_parts,
        'selected_equipment': equipment,
        'selected_targets': targets,
        'selected_sorting': selected_sorting,
    }

    return render(request, 'workouts/workouts.html', context)


def workout_detail(request, workout_id):
    """ A view to show workout details """

    workout = get_object_or_404(Workout, pk=workout_id)

    context = {
        'workout': workout,
    }

    return render(request, 'workouts/workout_detail.html', context)


@login_required
def add_workout(request):
    """Add a workout to the site"""
    if not request.user.is_superuser:
        messages.error(request, 'Super User permissions required')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = WorkoutForm(request.POST, request.FILES)
        if form.is_valid():
            workout = form.save()
            messages.success(request, 'Workout added')
            return redirect(reverse('workout_detail', args=[workout.id]))
        else:
            messages.error(
                request, 'Failed to add workout. Please ensure form is valid.')
    else:
        form = WorkoutForm()

    template = 'workouts/add_workout.html'
    context = {
        'form': form,
        'disable_add_to_bag': True,
    }

    return render(request, template, context)


@login_required
def edit_workout(request, workout_id):
    """Update a workout in the site"""
    if not request.user.is_superuser:
        messages.error(request, 'Super User permissions required')
        return redirect(reverse('home'))

    workout = get_object_or_404(Workout, pk=workout_id)
    if request.method == 'POST':
        form = WorkoutForm(request.POST, request.FILES, instance=workout)
        if form.is_valid():
            form.save()
            messages.success(request, 'Workout updated')
            return redirect(reverse('workout_detail', args=[workout.id]))
        else:
            messages.error(
                request, 'Failed to update workout. \
                    Please ensure form is valid.')
    else:
        form = WorkoutForm(instance=workout)
    messages.info(request, f'Editing {workout.name}')

    template = 'workouts/edit_workout.html'
    context = {
        'form': form,
        'workout': workout,
        'disable_add_to_bag': True,
    }

    return render(request, template, context)


@login_required
def delete_workout(request, workout_id):
    """Delete a workout from the site"""
    if not request.user.is_superuser:
        messages.error(request, 'Super User permissions required')
        return redirect(reverse('home'))

    workout = get_object_or_404(Workout, pk=workout_id)
    workout.delete()
    messages.success(request, 'Workout deleted')
    return redirect(reverse('workouts'))
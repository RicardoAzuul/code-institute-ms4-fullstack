from django.shortcuts import render
from .models import Feature

# Create your views here.


def index(request):
    """
    A view to return the index page
    """

    # Get all features from the db to populate on the index page
    features = Feature.objects.all()

    context = {
        'features': features,
    }

    return render(request, 'home/index.html', context)

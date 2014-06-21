# Create your views here.
from django.shortcuts import render


def index(request):
    """
    View for index site
    """

    return render(request, 'stilwiese/index.html')


def map(request):
    """
    View for site containing map
    """

    return render(request, 'stilwiese/map.html')
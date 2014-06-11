# Create your views here.
from django.shortcuts import render


def index(request):
    """
    View that gets the context variables for the index site body and renders the RequestContext
    """

    return render(request, 'stilwiese/base.html')
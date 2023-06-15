from django.shortcuts import render
from django.views.generic.edit import FormView

from .forms import *


# Create your views here.
def createBase_home(request):

    return render(request, 'createBase/createBase_home.html')

def materialSelection(request):

    return render(request, 'createBase/materialSelection.html')
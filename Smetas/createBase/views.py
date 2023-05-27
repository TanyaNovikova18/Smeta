from django.shortcuts import render
from django.views.generic.edit import FormView

from .forms import *


# Create your views here.
def createBase_home(request):
    #form = TypeSelection(request.POST)
    form = []
    if request.method == 'POST':
        form = request.POST.getlist('Тип сметы')

    return render(request, 'createBase/createBase_home.html', {'Тип сметы': form})

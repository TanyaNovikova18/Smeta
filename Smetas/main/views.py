from django.shortcuts import render
from .models import*
import pandas as pd

def index(request):
    return render(request, 'main/index.html')


def base(request):
    item = Base.objects.all().values()
    df = pd.DataFrame(item)
    mydict = {
        "df": df.to_html()
    }
    return render(request, 'main/base.html', context = mydict)



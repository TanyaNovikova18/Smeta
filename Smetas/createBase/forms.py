from django import forms
from .models import*

YEAR = (
    ('1', '1 год'),
    ('2', '2 года'),
    ('3', '3 года'),
)
class TypeSelection(forms.Form):
    at_this_moment = forms.BooleanField(required=False)
    intermediate = forms.BooleanField(required=False)
    if intermediate.required:
        years1 = forms.ChoiceField(choices=YEAR)
    delayed = forms.BooleanField(required=False)
    if delayed == True:
        years2 = forms.ChoiceField(choices=YEAR)

#class ChoicOne(forms.Form):
#    years1 = forms.ChoiceField(choices=YEAR)

#class ChoicTwo(forms.Form):
#    years2 = forms.ChoiceField(choices=YEAR)
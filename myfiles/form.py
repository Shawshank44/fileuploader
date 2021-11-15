from django import forms
from django.forms import fields
from.models import *

GENDER_CHOICES = [
    ('Male','Male'),
    ('Female','Female')
]

class User_form(forms.ModelForm):
     gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect(attrs={'class':'list-unstyled list-inline'}))

     class Meta:
         model = User_files
         fields = '__all__'
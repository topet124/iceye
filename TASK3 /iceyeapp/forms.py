from django import forms
from django.forms import ModelForm

from .models import *


class TaskForm(forms.Form):
    text = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Add a special name to the list of people.......', 'aria-label' : 'Todo', 'aria-describedby' :'add-btn'}))

    class Meta:
        model = List_name
        fields = '__all__'

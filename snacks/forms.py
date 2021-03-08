from django import forms
from .models import Snack


class InputForm(forms.Form):
    name = forms.CharField(label="Enter a snack", max_length=64)
    description = forms.CharField(widget=forms.Textarea)

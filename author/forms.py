from django import forms
from . import models
from .models import Author


class authorform (forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name','mail','desc','img']

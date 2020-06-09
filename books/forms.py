from django import forms
from . import models
from .models import Book


class bookform (forms.ModelForm):
    class Meta:
        model = Book
        fields = ['author','title','desc','img','state']

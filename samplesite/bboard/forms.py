from django.forms import ModelForm
from django import forms

from .models import *

class BbForm(ModelForm):
    class Meta:
        model = Bb
        fields = ("title", "content", "price", "image", "rubric")


class Cl(forms.Form):
    km = forms.IntegerField()

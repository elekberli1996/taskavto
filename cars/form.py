from django import forms
from .models import Cars

class CarForm(forms.ModelForm):
    class Meta:
        model=Cars
        fields=["marka","model","description"]
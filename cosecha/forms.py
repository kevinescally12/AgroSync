from django import forms
from django.forms import ModelForm
from .models import Terreno 

class TerrenoForm(ModelForm):
    class Meta: 
        model = Terreno
        fields = '__all__'
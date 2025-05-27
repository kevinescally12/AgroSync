from django import forms
from accounts.models import CustomUser
from .models import IngenieroAgricultores

class AsignarAgricultoresForm(forms.ModelForm):
    ingeniero = forms.ModelChoiceField(
        queryset=CustomUser.objects.filter(rol='ingeniero'),
        label="Ingeniero"
    )
    agricultores = forms.ModelMultipleChoiceField(
        queryset=CustomUser.objects.filter(rol='agricultor'),
        widget=forms.CheckboxSelectMultiple,
        label="Agricultores"
    )

    class Meta:
        model = IngenieroAgricultores
        fields = ['ingeniero', 'agricultores']

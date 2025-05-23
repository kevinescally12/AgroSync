from django import forms
from .models import Terreno


from django import forms
from .models import Terreno
from accounts.models import CustomUser

class TerrenoForm(forms.ModelForm):
    class Meta:
        model = Terreno
        fields = ['nombre', 'ubicacion', 'area', 'agricultor']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Limitar opciones del campo agricultor a usuarios con rol 'agricultor'
        self.fields['agricultor'].queryset = CustomUser.objects.filter(rol='agricultor')

from django import forms
from .models import Structure


class StructureForm(forms.ModelForm):
    class Meta:
        model = Structure
        fields = ['address']
        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'address': 'Введите адрес здания',
        }

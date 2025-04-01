from django import forms
from .models import RegAtrasos

class RegistroAtrasoForm(forms.ModelForm):
    class Meta:
        model = RegAtrasos
        fields = ['data_atraso', 'horario_chegada', 'justificativa']
        widgets = {
            'data_atraso': forms.DateInput(attrs={'type': 'date'}),
            'horario_chegada': forms.TimeInput(attrs={'type': 'time'}),
        }
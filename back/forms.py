from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Tarea


class NuevaTareaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('', 'Guardar'))

    class Meta:
        model = Tarea
        fields = ['tarea', 'vencimiento']
        widgets = {
            'vencimiento': forms.TextInput(attrs={'type': 'datetime-local'}),
        }


class BorrarTareaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('', 'Aceptar'))

    class Meta:
        model = Tarea
        fields = []


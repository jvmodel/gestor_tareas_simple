from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Tarea


class NuevaTareaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('guardar', 'Guardar'))

    class Meta:
        model = Tarea
        fields = ['tarea', 'vencimiento']
        widgets = {
            'vencimiento': forms.TextInput(attrs={'type': 'datetime-local'}),
        }


class EditarTareaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('', 'Guardar', css_class='btn-success'))
        self.helper.add_input(Submit('borrar', 'Eliminar', css_class='btn-danger'))
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
        self.helper.add_input(Submit('', 'Eliminar', css_class='btn-danger'))

    class Meta:
        model = Tarea
        fields = []


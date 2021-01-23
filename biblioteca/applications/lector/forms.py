from django import forms
from .models import prestamo


class PrestamoForms(forms.ModelForm):



    class Meta:
        model = prestamo
        fields = ('lector', 'libro',)

        
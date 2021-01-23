from datetime import date
from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import PrestamoForms
from .models import prestamo

# Create your views here.
class RegistrarPrestamo(FormView):
    template_name = 'lector/add_prestamo.html'
    form_class = PrestamoForms
    success_url = '.'

    def form_valid(self, form):

        """prestamo.objects.create(
            lector=form.cleaned_data['lector'],
            libro=form.cleaned_data['libro'],
            fecha_prestamo=date.today(),
            devuelto=False
        )"""

        preestamo=prestamo(
            lector=form.cleaned_data['lector'],
            libro=form.cleaned_data['libro'],
            fecha_prestamo=date.today(),
            devuelto=False
        )
        preestamo.save()

        return super(RegistrarPrestamo, self).form_valid(form)



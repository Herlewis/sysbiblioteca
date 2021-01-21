from django.db import models
from django.db.models import Q, Avg, Sum, Count
from django.db.models.functions import Lower

class PrestamoManager(models.Manager):
    """Managers para el modelo prestamo"""
    def libros_promedio_edades(self):
        resultado =self.filter(

            libro__id='3'
        ).aggregate(
            promedio_edad=Avg('lector__edad'),
            suma_edad=Sum('lector__edad'),
        )
        return resultado

    def num_libros_prestados(self):
        resultado = self.values('libro').annotate(
            titulo = Lower('libro__titulo'),
            num_prestados = Count('libro'),
        )
        for r in resultado:
            print('=================')
            print(r, r['num_prestados'])
        return resultado
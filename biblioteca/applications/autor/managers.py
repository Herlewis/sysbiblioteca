from django.db import models
from django.db.models import Q

class AutorManager(models.Manager):
    """Managers para el modelo Autor"""

    """Por palabra clave"""
    def buscar_autor(self, kword):

        resultado = self.filter(nombre__icontains=kword)

        return resultado

    """OR"""

    def buscar_autor2(self, kword):

        resultado = self.filter(Q(nombre__icontains=kword ) | Q(apellidos__icontains=kword ))

        return resultado

    """Excluir"""
    
    def buscar_autor3(self, kword):

        resultado = self.filter(
            nombre__icontains=kword
        ).exclude(Q(edad__icontains=25 ) | Q(edad__icontains=40 ))

        return resultado

    """AND"""
    def buscar_autor4(self, kword):

        resultado = self.filter(edad__gt=40, edad__lt = 60 ).order_by('apellidos')

        return resultado
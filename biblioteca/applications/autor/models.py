from django.db import models

#managers Autor
from .managers import AutorManager

# Create your models here.
class Persona(models.Model):
    """Model definition for Autor."""
    nombres = models.CharField( max_length=50)
    apellidos = models.CharField( max_length=50)
    nacionalidad = models.CharField( max_length=30)
    edad = models.PositiveIntegerField()

    
    class Meta:
        """Meta definition for Autor."""

        abstract = True

    def __str__(self):
        """Unicode representation of Autor."""
        return str(self.id) +'-'+ self.nombres + ' - ' + self.apellidos 

class Autor(Persona):

    objects = AutorManager()    

    class Meta:
        """Meta definition for Autor."""

        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

   


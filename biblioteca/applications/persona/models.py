from django.db import models

class Persona(models.Model):
    """Model definition for Persona."""

    full_name = models.CharField('Nombres', max_length=50)
    pais = models.CharField('Pais', max_length=30)
    pasaporte = models.CharField('Pasaporte', max_length=50)
    edad = models.IntegerField()
    apelativo = models.CharField('Apelativos', max_length=50)

    class Meta:
        """Meta definition for Persona."""

        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        db_table = 'persona'
        unique_together =['pais', 'apelativo']
        constraints = [
            models.CheckConstraint( check = models.Q(edad__gte=18 ), name = 'edad_mayor_18')
        ]

        abstract=True

    def __str__(self):
        """Unicode representation of Persona."""
        return self.full_name

class Empleados(Persona):
    empleo = models.CharField('Empleo', max_length=50)


class Cliente(Persona):
    email = models.EmailField('Email')


# Create your models here.

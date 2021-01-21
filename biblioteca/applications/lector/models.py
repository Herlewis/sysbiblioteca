from django.db import models

from applications.libro.models import Libro

from .managers import PrestamoManager


class Lector(models.Model):
    """Model definition for Lector."""

    nombre = models.CharField( max_length=50)
    apellitos = models.CharField( max_length=50)
    nacionalidad = models.CharField( max_length=50)
    edad = models.PositiveIntegerField(default= 0)

    class Meta:
        """Meta definition for Lector."""

        verbose_name = 'Lector'
        verbose_name_plural = 'Lectores'

    def __str__(self):
        """Unicode representation of Lector."""
        return self.nombre


class prestamo(models.Model):
    """Model definition for prestamo."""

    lector = models.ForeignKey(Lector, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='libro_prestamo')
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField(blank=True, null=True)
    devuelto = models.BooleanField()

    objects = PrestamoManager()
    

    class Meta:
        """Meta definition for prestamo."""

        verbose_name = 'prestamo'
        verbose_name_plural = 'prestamos'

    def __str__(self):
        """Unicode representation of prestamo."""
        return self.libro.titulo





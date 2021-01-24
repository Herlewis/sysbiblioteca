from django.db import models

from applications.libro.models import Libro
from applications.autor.models import Persona
from django.db.models.signals import post_delete

from .managers import PrestamoManager


class Lector(Persona):
    """Model definition for Lector."""

    class Meta:
        """Meta definition for Lector."""

        verbose_name = 'Lector'
        verbose_name_plural = 'Lectores'


class Prestamo(models.Model):
    """Model definition for prestamo."""

    lector = models.ForeignKey(Lector, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='libro_prestamo')
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField(blank=True, null=True)
    devuelto = models.BooleanField()

    objects = PrestamoManager()

    def save(self, *args, **kwargs):

        self.libro.stock = self.libro.stock - 1
        self.libro.save()

        super(Prestamo, self).save(*args, **kwargs)
    

    class Meta:
        """Meta definition for prestamo."""

        verbose_name = 'Prestamo'
        verbose_name_plural = 'Prestamos'

    def __str__(self):
        """Unicode representation of prestamo."""
        return self.libro.titulo

def update_libro_stock(sender, instance, **kwargs):
    instance.libro.stock = instance.libro.stock + 1
    instance.libro.save()

post_delete.connect(update_libro_stock, sender=Prestamo)





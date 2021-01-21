from django.db import models
from applications.autor.models import Autor

#Managers
from .managers import LibroManager, CategoriaManager

# Create your models here.
class Categoria(models.Model):
    """Model definition for Categoria."""

    nombre = models.CharField( max_length=30)

    objects = CategoriaManager()

    class Meta:
        """Meta definition for Categoria."""

        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        """Unicode representation of Categoria."""
        return self.nombre

class Libro(models.Model):
    """Model definition for Libro."""

    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.CASCADE,
        related_name = 'categoria_libro'
    )
    autores = models.ManyToManyField(Autor)    
    titulo = models.CharField( max_length=50)
    fecha = models.DateField('Fecha de lanzamiento')
    portada = models.ImageField( upload_to='portada', null=True)
    visitas = models.PositiveIntegerField()


    objects = LibroManager()

    class Meta:
        """Meta definition for Libro."""

        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'

    def __str__(self):
        """Unicode representation of Libro."""
        return str(self.id) + ' - ' + self.titulo


# Create your models here.

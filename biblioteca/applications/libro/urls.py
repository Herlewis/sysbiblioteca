from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('libros-trg/', views.ListLibrosTrg.as_view(), name = 'libros-trg'),
    path('libros/', views.ListLibros.as_view(), name = 'libros'),
    path('libro-detalle/<pk>/', views.LibroDetailView.as_view(), name = 'libro-detalle'),
]
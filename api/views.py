from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Producto, Tienda, Usuario
from .serializers import ProductoSerializer, TiendaSerializer, UsuarioSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all().order_by('id')
    serializer_class = UsuarioSerializer


class TiendaViewSet(viewsets.ModelViewSet):
    queryset = Tienda.objects.select_related('propietario').all().order_by('id')
    serializer_class = TiendaSerializer


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.select_related('tienda').all().order_by('id')
    serializer_class = ProductoSerializer

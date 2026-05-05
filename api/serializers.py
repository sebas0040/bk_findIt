from rest_framework import serializers
from .models import Producto, Tienda, Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'


class TiendaSerializer(serializers.ModelSerializer):
    propietario_nombre = serializers.CharField(source='propietario.nombre', read_only=True)

    class Meta:
        model = Tienda
        fields = [
            'id',
            'nombre',
            'descripcion',
            'direccion',
            'ciudad',
            'activa',
            'fecha_creacion',
            'propietario',
            'propietario_nombre',
        ]


class ProductoSerializer(serializers.ModelSerializer):
    tienda_nombre = serializers.CharField(source='tienda.nombre', read_only=True)

    class Meta:
        model = Producto
        fields = [
            'id',
            'nombre',
            'precio',
            'descripcion',
            'stock',
            'tienda',
            'tienda_nombre',
        ]

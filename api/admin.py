from django.contrib import admin
from .models import Producto, Tienda, Usuario

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Tienda)
admin.site.register(Producto)

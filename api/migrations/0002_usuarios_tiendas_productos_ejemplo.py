# Generated for adding users, stores, and sample data.

from django.db import migrations, models
import django.db.models.deletion


def crear_datos_ejemplo(apps, schema_editor):
    Usuario = apps.get_model('api', 'Usuario')
    Tienda = apps.get_model('api', 'Tienda')
    Producto = apps.get_model('api', 'Producto')

    usuarios_data = [
        {
            'nombre': 'Ana Gomez',
            'correo': 'ana.gomez@example.com',
            'telefono': '3001234567',
            'direccion': 'Calle 10 #20-30',
        },
        {
            'nombre': 'Carlos Perez',
            'correo': 'carlos.perez@example.com',
            'telefono': '3109876543',
            'direccion': 'Carrera 7 #15-45',
        },
        {
            'nombre': 'Laura Martinez',
            'correo': 'laura.martinez@example.com',
            'telefono': '3205557788',
            'direccion': 'Avenida Siempre Viva #123',
        },
    ]

    usuarios = {}
    for data in usuarios_data:
        usuario, _ = Usuario.objects.get_or_create(
            correo=data['correo'],
            defaults={
                'nombre': data['nombre'],
                'telefono': data['telefono'],
                'direccion': data['direccion'],
            },
        )
        usuarios[data['correo']] = usuario

    tiendas_data = [
        {
            'nombre': 'TechZone',
            'descripcion': 'Tienda de tecnologia, computadores y accesorios.',
            'direccion': 'Centro Comercial Norte Local 205',
            'ciudad': 'Pasto',
            'propietario': usuarios['ana.gomez@example.com'],
        },
        {
            'nombre': 'Moda Urbana',
            'descripcion': 'Ropa casual, calzado y accesorios juveniles.',
            'direccion': 'Calle 18 #24-60',
            'ciudad': 'Pasto',
            'propietario': usuarios['carlos.perez@example.com'],
        },
        {
            'nombre': 'Hogar Plus',
            'descripcion': 'Articulos para el hogar, cocina y decoracion.',
            'direccion': 'Avenida Panamericana #9-80',
            'ciudad': 'Pasto',
            'propietario': usuarios['laura.martinez@example.com'],
        },
    ]

    tiendas = {}
    for data in tiendas_data:
        tienda, _ = Tienda.objects.get_or_create(
            nombre=data['nombre'],
            defaults={
                'descripcion': data['descripcion'],
                'direccion': data['direccion'],
                'ciudad': data['ciudad'],
                'propietario': data['propietario'],
            },
        )
        tiendas[data['nombre']] = tienda

    productos_data = [
        {
            'nombre': 'Laptop Lenovo IdeaPad',
            'precio': '2500000.00',
            'descripcion': 'Portatil para estudio y trabajo diario.',
            'stock': 8,
            'tienda': tiendas['TechZone'],
        },
        {
            'nombre': 'Mouse Inalambrico',
            'precio': '55000.00',
            'descripcion': 'Mouse ergonomico con conexion USB.',
            'stock': 30,
            'tienda': tiendas['TechZone'],
        },
        {
            'nombre': 'Chaqueta Denim',
            'precio': '120000.00',
            'descripcion': 'Chaqueta clasica en jean azul.',
            'stock': 12,
            'tienda': tiendas['Moda Urbana'],
        },
        {
            'nombre': 'Set de Ollas',
            'precio': '180000.00',
            'descripcion': 'Juego de ollas antiadherentes de 5 piezas.',
            'stock': 10,
            'tienda': tiendas['Hogar Plus'],
        },
    ]

    for data in productos_data:
        if not Producto.objects.filter(nombre=data['nombre']).exists():
            Producto.objects.create(**data)


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=254, unique=True)),
                ('telefono', models.CharField(blank=True, max_length=20)),
                ('direccion', models.CharField(blank=True, max_length=150)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tienda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('descripcion', models.TextField(blank=True, default='')),
                ('direccion', models.CharField(max_length=150)),
                ('ciudad', models.CharField(max_length=80)),
                ('activa', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('propietario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tiendas', to='api.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='descripcion',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='producto',
            name='stock',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='producto',
            name='tienda',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='productos', to='api.tienda'),
        ),
        migrations.RunPython(crear_datos_ejemplo, migrations.RunPython.noop),
    ]

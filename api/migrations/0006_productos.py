# Generated by Django 5.1.2 on 2024-10-29 01:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_administradores'),
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.IntegerField(default=0)),
                ('imagen_url', models.CharField(blank=True, max_length=255, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('id_categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.categorias')),
                ('id_proveedor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.proveedores')),
            ],
            options={
                'db_table': 'productos',
            },
        ),
    ]

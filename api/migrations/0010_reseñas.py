# Generated by Django 5.1.2 on 2024-10-29 01:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_inventario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reseñas',
            fields=[
                ('id_resena', models.AutoField(primary_key=True, serialize=False)),
                ('calificacion', models.IntegerField()),
                ('comentario', models.TextField(blank=True, null=True)),
                ('fecha_resena', models.DateTimeField(auto_now_add=True)),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.clientes')),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.productos')),
            ],
            options={
                'db_table': 'resenas',
            },
        ),
    ]

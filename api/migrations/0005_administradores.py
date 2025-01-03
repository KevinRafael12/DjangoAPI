# Generated by Django 5.1.2 on 2024-10-29 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_clientes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administradores',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('password_hash', models.CharField(max_length=255)),
                ('rol', models.CharField(choices=[('Admin', 'Admin'), ('Empleado', 'Empleado')], default='Empleado', max_length=8)),
            ],
            options={
                'db_table': 'administradores',
            },
        ),
    ]

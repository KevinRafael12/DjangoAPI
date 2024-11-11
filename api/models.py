from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Generos (models.Model):
    genero_id = models.AutoField(primary_key=True)
    tipo_genero = models.CharField(max_length=255)
    
    class Meta:
        db_table = "generos"
        
class Usuarios(models.Model):
    usuarios_id = models.AutoField(primary_key=True)
    nombre_completo = models.CharField(max_length=255)
    fk_generos = models.ForeignKey(Generos,on_delete=models.CASCADE)
    
    class Meta:
        db_table = "usuarios"

class Categorias(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    class Meta:
        db_table = "categorias"


class Proveedores(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100, null=True, blank=True)  
    telefono = models.CharField(max_length=15, null=True, blank=True)    
    email = models.CharField(max_length=100, null=True, blank=True)      
    direccion = models.TextField(null=True, blank=True)                  

    class Meta:
        db_table = "proveedores"


class Clientes(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True) 
    telefono = models.CharField(max_length=15, null=True, blank=True)  
    direccion = models.TextField(null=True, blank=True)               
    fecha_registro = models.DateTimeField(auto_now_add=True)          

    class Meta:
        db_table = "clientes"


class Administradores(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    password_hash = models.CharField(max_length=255)
    rol = models.CharField(
        max_length=8, 
        choices=[('Admin', 'Admin'), ('Empleado', 'Empleado')], 
        default='Empleado'
    )

    class Meta:
        db_table = "administradores"
        

class Productos(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)  
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    id_categoria = models.ForeignKey(Categorias, on_delete=models.SET_NULL, null=True, blank=True)
    id_proveedor = models.ForeignKey(Proveedores, on_delete=models.SET_NULL, null=True, blank=True)
    stock = models.IntegerField(default=0)
    imagen_url = models.CharField(max_length=255, null=True, blank=True)  
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "productos"



class Pedidos(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)  
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  
    estado = models.CharField(max_length=50, default='Pendiente')  

    class Meta:
        db_table = "pedidos"


class DetallesPedido(models.Model):
    id_detalle = models.AutoField(primary_key=True)
    id_pedido = models.ForeignKey(Pedidos, on_delete=models.CASCADE)  
    id_producto = models.ForeignKey(Productos, on_delete=models.CASCADE)  
    cantidad = models.IntegerField()  
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  

    class Meta:
        db_table = "detalles_pedido"



class Inventario(models.Model):
    id_inventario = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey(Productos, on_delete=models.CASCADE)  
    cantidad = models.IntegerField()  
    fecha_actualizacion = models.DateTimeField(auto_now=True)  

    class Meta:
        db_table = "inventario"



class Reseñas(models.Model):
    id_resena = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey(Productos, on_delete=models.CASCADE)  
    id_cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)  
    calificacion = models.IntegerField()  
    comentario = models.TextField(null=True, blank=True)  
    fecha_resena = models.DateTimeField(auto_now_add=True) 

    class Meta:
        db_table = "resenas"

    def clean(self):
        if not (1 <= self.calificacion <= 5):
            raise ValidationError('La calificación debe estar entre 1 y 5.')

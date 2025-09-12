from django.db import models
from django.contrib.auth.models import AbstractUser

# Roles
class Rol(models.Model):
    nombre_rol = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre_rol


# Usuarios
class Usuario(AbstractUser):
    email = models.EmailField(unique=True)
    #rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    rol = models.ForeignKey(Rol, null=True, blank=True, on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.username} ({self.rol})"


# Residentes
class Residente(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    numero_apartamento = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.usuario.username} - {self.numero_apartamento}"


# Áreas Comunes
class AreaComun(models.Model):
    nombre_area = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    costo_por_hora = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    costo_por_dia = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    capacidad = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.nombre_area


# Reservas
class Reserva(models.Model):
    ESTADOS = (
        ('Pendiente', 'Pendiente'),
        ('Pagado', 'Pagado'),
        ('Cancelado', 'Cancelado'),
    )

    residente = models.ForeignKey(Residente, on_delete=models.CASCADE)
    area = models.ForeignKey(AreaComun, on_delete=models.CASCADE)
    fecha_reserva = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='Pendiente')
    codigo_qr = models.CharField(max_length=255, blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reserva {self.id} - {self.area.nombre_area}"


# Facturas
class Factura(models.Model):
    ESTADOS = (
        ('Pendiente', 'Pendiente'),
        ('Pagada', 'Pagada'),
        ('Atrasada', 'Atrasada'),
    )

    residente = models.ForeignKey(Residente, on_delete=models.CASCADE)
    fecha_emision = models.DateField()
    fecha_vencimiento = models.DateField()
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='Pendiente')
    ruta_pdf = models.CharField(max_length=255, blank=True, null=True)
    codigo_qr = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Factura {self.id} - {self.residente.usuario.username}"


# Pagos
class Pago(models.Model):
    residente = models.ForeignKey(Residente, on_delete=models.CASCADE)
    factura = models.ForeignKey(Factura, on_delete=models.SET_NULL, null=True, blank=True)
    reserva = models.ForeignKey(Reserva, on_delete=models.SET_NULL, null=True, blank=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateTimeField(auto_now_add=True)
    metodo_pago = models.CharField(max_length=100)
    referencia = models.CharField(max_length=255)

    def __str__(self):
        return f"Pago {self.id} - {self.residente.usuario.username}"

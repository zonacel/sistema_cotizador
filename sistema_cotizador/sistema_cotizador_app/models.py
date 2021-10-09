from django.db import models

# Create your models here.
# Modelos - clases que tiene el proyecto
#


class cliente(models.Model):
    # datos de clientes
    created = models.DateTimeField("creado", auto_now_add=True)
    modified = models.DateTimeField("modificado", auto_now=True)
    nombre = models.CharField(max_length=80)
    tipo_cliente = models.CharField(max_length=40)
    cargo = models.CharField(max_length=40)
    # blank and null para hacer que no sea campo requerido en el admin.py
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class producto_servicio(models.Model):
    # datos de productos y servicios
    created = models.DateTimeField(
        verbose_name=("creado"), auto_now_add=True)
    modified = models.DateTimeField("modificado", auto_now=True)
    tipo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=80)
    valor_neto = models.DecimalField(decimal_places=2,
                                     max_digits=8,
                                     null=True)
    status = models.BooleanField(verbose_name=('estado'),
                                 default=True)
    margen = models.DecimalField(decimal_places=2,
                                 max_digits=8,
                                 null=True)
    especificacion_tecnica = models.CharField(max_length=300)
    unidad_medida = models.CharField(max_length=10)

    # funcion que devuelve el __str__ del modelo
    def tipo_nombre(self):
        return '%s: %s' % (self.tipo, self.nombre)

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
# Create your models here.
# Modelos - clases que tiene el proyecto
#


class catalogo_ruc_dni(models.Model):
    nombre = models.CharField(max_length=500)
    tipo_documento = models.PositiveIntegerField(
        validators=[MaxValueValidator(99)])
    numero_documento = models.CharField(max_length=11)
    estado = models.CharField(max_length=20)
    condicion = models.CharField(max_length=20)
    direccion = models.CharField(max_length=500)
    ubigeo = models.CharField(max_length=8)
    via_tipo = models.CharField(max_length=15)
    via_nombre = models.CharField(max_length=30)
    zona_codigo = models.CharField(max_length=30)
    zona_tipo = models.CharField(max_length=30)
    numero = models.IntegerField()
    interior = models.CharField(max_length=30)
    lote = models.CharField(max_length=30)
    dpto = models.CharField(max_length=30)
    manzana = models.CharField(max_length=30)
    kilometro = models.CharField(max_length=30)
    distrito = models.CharField(max_length=30)
    provincia = models.CharField(max_length=30)
    departamento = models.CharField(max_length=30)


class cliente(models.Model):
    # datos de clientes
    created = models.DateTimeField("creado", auto_now_add=True)
    modified = models.DateTimeField("modificado", auto_now=True)
    nombre = models.CharField(max_length=80)
    tipo_cliente = models.CharField(max_length=40)
    cargo = models.CharField(max_length=40)
    # blank and null para hacer que no sea campo requerido en el admin.py
    email = models.EmailField(blank=True, null=True)
    id_persona_catalogo_ruc_dni = models.ForeignKey(
        catalogo_ruc_dni, related_name='id_persona_catalogo_ruc_dni', verbose_name="persona catalogo ruc dni", null=True, blank=True, on_delete=models.SET_NULL)
    id_empresa_catalogo_ruc_dni = models.ForeignKey(
        catalogo_ruc_dni, related_name='id_empresa_catalogo_ruc_dni', verbose_name="empresa catalogo ruc dni", null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nombre


class producto_servicio(models.Model):
    # datos de productos y servicios
    created = models.DateTimeField(
        verbose_name=("fecha registro"), auto_now_add=True)
    modified = models.DateTimeField("multima actualizacion", auto_now=True)
    tipo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=80)
    valor_neto = models.DecimalField(decimal_places=2,
                                     max_digits=8,
                                     default=0)
    status = models.BooleanField(verbose_name=('estado'),
                                 default=True)
    margen = models.DecimalField(decimal_places=2,
                                 max_digits=8,
                                 null=True)
    especificacion_tecnica = models.CharField(max_length=300)
    unidad_medida = models.CharField(max_length=10, null=True, blank=True)

    # funcion que devuelve el __str__ del modelo
    def tipo_nombre(self):
        return '%s: %s' % (self.tipo, self.nombre)


class catalogo_tipo_cambio(models.Model):
    fecha = models.DateField(auto_now_add=True, unique=True)
    compra = models.DecimalField(decimal_places=2,
                                 max_digits=5,
                                 null=True)
    venta = models.DecimalField(decimal_places=2,
                                max_digits=5,
                                null=True)
    origen = models.CharField(max_length=100)
    moneda = models.CharField(max_length=20)


class cotizador_maestro(models.Model):
    created = models.DateTimeField(
        verbose_name=("fecha reigstro"), auto_now_add=True)
    modified = models.DateTimeField(verbose_name=(
        "ultima actualizacion"), auto_now=True)
    nombre_proyecto = models.CharField(max_length=200)
    id_usuario = models.ForeignKey(
        User, related_name='id_usuario', verbose_name="id usuario", null=True, blank=True, on_delete=models.SET_NULL)
    id_cliente = models.ForeignKey(
        cliente, verbose_name="id cliente", null=True, blank=True, on_delete=models.SET_NULL)
    id_catalogo_tipo_cambio = models.ForeignKey(
        catalogo_tipo_cambio, related_name='id_catalogo_tipo_cambio', verbose_name="id_catalogo_tipo_cambio", null=True, blank=True, on_delete=models.SET_NULL)


class cotizador_detalle(models.Model):
    id_cotizador_maestro = models.ForeignKey(
        cotizador_maestro, verbose_name="id cotizador maestro", null=True, blank=True, on_delete=models.CASCADE)
    id_producto_servicio = models.ForeignKey(
        producto_servicio, verbose_name="id producto servicio", null=True, blank=True, on_delete=models.SET_NULL)

    def producto_detalle(self):
        return self.producto_servicio


class fichero(models.Model):
    fecha = models.DateField(auto_now_add=True)
    nombre = models.CharField(max_length=100)
    path = models.CharField(max_length=100)
    id_cotizador_maestro = models.ForeignKey(
        cotizador_maestro, verbose_name="id cotizador maestro", null=True, blank=True, on_delete=models.SET_NULL)

from django.contrib import admin
# Register your models here.

# importando el modelo
from sistema_cotizador_app.models import cliente
from sistema_cotizador_app.models import producto_servicio

# ModelAdmin que nos permite realizar cambios en el admin, heredando los valores a mostrar


class clienteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "cargo", "email")
    search_fields = ("nombre", "email")  # busqueda en el admin
    list_filter = ("cargo",)  # indicando como sera el filtro


class producto_servicioAdmin(admin.ModelAdmin):
    list_display = ("tipo_nombre", "valor_neto", "status", "unidad_medida")
    search_fields = ("nombre", "tipo")  # busqueda en el admin
    list_filter = ("unidad_medida", "created",)
    date_hierarchy = ("created")


# se agrega los registros de la clase cliente y la nueva clase clienteAdmin
admin.site.register(cliente, clienteAdmin)
admin.site.register(producto_servicio, producto_servicioAdmin)

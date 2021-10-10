from django.contrib import admin
# Register your models here.

# importando el modelo
from sistema_cotizador_app.models import cliente
from sistema_cotizador_app.models import producto_servicio
from sistema_cotizador_app.models import cotizador_maestro
from sistema_cotizador_app.models import cotizador_detalle
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


class cotizador_maestroAdmin(admin.ModelAdmin):
    list_display = ("nombre_proyecto", "id_usuario")
    search_fields = ("nombre_proyecto", "id_usuario")
    list_filter = ("id_usuario", "id_cliente",)
    date_hierarchy = ("created")


class cotizador_detalleAdmin(admin.ModelAdmin):
    list_display = ("id_cotizador_maestro", "producto_detalle")
    #search_fields = ("id_cotizador_maestro", "id_usuario")


# se agrega los registros de la clase cliente y la nueva clase clienteAdmin
admin.site.register(cliente, clienteAdmin)
admin.site.register(producto_servicio, producto_servicioAdmin)
admin.site.register(cotizador_maestro, cotizador_maestroAdmin)
admin.site.register(cotizador_detalle, cotizador_detalleAdmin)

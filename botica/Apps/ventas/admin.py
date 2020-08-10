from django.contrib import admin
from .models import Cabecera_Venta,todo_item
# Register your models here.
class medicamento_ventaInline(admin.TabularInline):
    model = todo_item

class Detalle_VentaAdmin(admin.ModelAdmin):
    inlines = (medicamento_ventaInline,)

admin.site.register(Cabecera_Venta, Detalle_VentaAdmin)
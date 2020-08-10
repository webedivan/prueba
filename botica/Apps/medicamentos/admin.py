from django.contrib import admin
from .models import Presentacion,Medicamento
# Register your models here.
@admin.register(Presentacion)
class PresentacionAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

@admin.register(Medicamento)
class MedicamentoAdmin(admin.ModelAdmin):
    list_display = (
    'lote', 'presentacion','tipo' ,'nombre', 'componente','concentracion', 'fecha_expiracion', 'fecha_produccion', 'precio_compra',
    'descripcion','precio_compra','precio_venta', 'stock','igv')
    search_fields = ('nombre', 'descripcion')

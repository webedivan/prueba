from django.contrib import admin
from .models import Distribuidor
# Register your models here.
@admin.register(Distribuidor)
class DistribuidorAdmin(admin.ModelAdmin):
    list_display =['razonSocial','ruc','telefono','direccion']
    list_display_links = ['razonSocial','ruc']
    search_fields = ['razonSocial','ruc']
from django.contrib import admin
from .models import Laboratorio
# Register your models here.
@admin.register(Laboratorio)
class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ['codigo','nombre','sanitario','autorizacion']
    list_display_links = ['codigo','nombre']
    search_fields = ['codigo','nombre']
from django.contrib import admin

from .models import cliente
# Register your models here.
admin.site.site_url = None # null
admin.site.site_header = 'BOTICA AYALA'
@admin.register(cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nombre','apellidos','dni','sexo','celular']
    list_display_links =['nombre','apellidos','dni','celular']
    search_fields = ['nombre','apellidos','dni']
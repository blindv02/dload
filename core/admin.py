from django.contrib import admin
from .models import Usuarios

admin.site.site_header="Dload!"
admin.site.index_title="Administracion del sitio"
admin.site.site_title="Dload - Administracion"

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('apellido','nombre','email','password','fecha_alta',)
    
    search_fields = ['apellido','email']
    
# Register your models here.
admin.site.register(Usuarios, UsuarioAdmin)


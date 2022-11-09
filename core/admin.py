from django.contrib import admin
from .models import Usuarios
from .models import Historia_descarga

admin.site.site_header="Dload!"
admin.site.index_title="Administracion del sitio"
admin.site.site_title="Dload - Administracion"

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('apellido','nombre','email','password','fecha_alta',)
    
    search_fields = ['apellido','email']



class Historia_descargaAdmin(admin.ModelAdmin):
    
    list_display = ('fecha','user_email','descargas','url','titulo')
    search_fields = ['fecha','user_email']

    
# Register your models here.
admin.site.register(Usuarios, UsuarioAdmin)
admin.site.register(Historia_descarga,Historia_descargaAdmin)


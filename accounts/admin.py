from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario
from django.utils.html import format_html

admin.site.site_header="Dload!"
admin.site.index_title="Administracion del sitio"
admin.site.site_title="Para uso exclusivo de Enrique - Leo y Pablo"


class UsuarioAdmin(UserAdmin):
    list_display = ('email', 'nombre','apellido', 'ultimo_login', 'fecha_alta')
    list_display_link = ('email', 'nombre', 'apellido')
    readonly_fields = ('ultimo_login', 'fecha_alta')
    ordering = ('-fecha_alta',)

    filter_horizontal=()
    list_filter = ()
    fieldsets = ()


# Register your models here.
admin.site.register(Usuario)

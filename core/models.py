from django.db import models

# Create your models here.
class Usuarios(models.Model):
    nombre = models.CharField(max_length=50,verbose_name='Nombre')
    apellido = models.CharField(max_length=50,verbose_name='Apellido')
    email = models.CharField(max_length=100, unique=True,verbose_name='Email')
    password = models.CharField(max_length=50,verbose_name='Contraseña')
    fecha_alta = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de Alta')
        
    REQUIRED_FIELDS = ['email', 'password', 'nombre','apellido']
    
    def nombre_completo(self):
        return f'{self.nombre}, {self.apellido}'
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        ordering = ['-fecha_alta']
  
    def __str__(self):
        return self.email

# Agregado por Leo para hacer el historial de desacarga#
######################## 5/11/2022 #####################
class Historia_descarga(models.Model):
    fecha = models.DateField(auto_now_add=True,verbose_name='Fecha de Búsqueda')
    user_email = models.EmailField(max_length=50, verbose_name="email")
    tipo_descarga = models.CharField(max_length=3,verbose_name='Tipo Descarga')
    url = models.URLField(verbose_name='URL')
    descargas = models.SmallIntegerField(verbose_name='Cantidad de Descargas')
    titulo = models.CharField(max_length = 100,verbose_name='Título')
    
    
    def __str__(self):
        return f'{self.pk},{self.fecha},{self.titulo},{self.user_email},{self.url},{self.descargas},{self.tipo_descarga}'
    
    def info_descarga(self):
        return f'{self.fecha},{self.titulo},{self.url},{self.descargas},{self.tipo_descarga}'
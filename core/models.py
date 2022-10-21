from django.db import models

# Create your models here.
class Usuarios(models.Model):
    nombre = models.CharField(max_length=50,verbose_name='Nombre')
    apellido = models.CharField(max_length=50,verbose_name='Apellido')
    email = models.CharField(max_length=100, unique=True,verbose_name='Email')
    password = models.CharField(max_length=50,verbose_name='Contraseña')
    fecha_alta = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de Alta')
        
    REQUIRED_FIELDS = ['email', 'password', 'nombre','apellido']
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        ordering = ['-fecha_alta']
  
    def __str__(self):
        return self.email

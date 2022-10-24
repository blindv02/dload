from django.db import models

# Create your models here.

class Usuarios(models.Model):
    nombre = models.CharField(max_length=30, null=False)
    correo_electronico = models.EmailField()
    fecha_registro = models.DateField.auto_now_add()
    
class Multimedia(models.Model):
    nombre = models.ForeignKey(Usuarios, null=True, blank=True, on_delete=models.CASCADE)
    titulo = models.CharField(null=False)
    embed_link = models.URLField()
    
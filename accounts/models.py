from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.
class UsuariosManager(BaseUserManager):
    def create_user(self, nombre, apellido, email, password=None):
        if not email:
            raise ValueError('el usuario debe tener un email')

        user = self.model(
            email = self.normalize_email(email),
            nombre = nombre,
            apellido = apellido,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, nombre, apellido, email, password):
        user = self.create_user(
        email = self.normalize_email(email),
        password = password,
        nombre = nombre,
        apellido = apellido,
        )

        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user


class Usuario(AbstractBaseUser):
    nombre = models.CharField(max_length=50,verbose_name='Nombre')
    apellido = models.CharField(max_length=50,verbose_name='Apellido')
    email = models.EmailField(max_length = 50,verbose_name='Email',unique=True)

    #campos atributos de django
    fecha_alta = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de registro')
    ultimo_login = models.DateTimeField(auto_now_add=True,verbose_name='Ultimo login')
    is_admin = models.BooleanField(default=True,verbose_name='Administrador')
    is_staff = models.BooleanField(default=True,verbose_name='Staff')
    is_active = models.BooleanField(default=True,verbose_name='Activo')
    is_superadmin = models.BooleanField(default=True,verbose_name='Superadmin')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre','apellido']

    objects = UsuariosManager()
    class Meta:
        verbose_name = "Cuenta de Usuario"
        verbose_name_plural = "Cuentas de Usuarios"
        ordering = ['fecha_alta']
        
   
    def nombre_completo(self):
        return f'{self.nombre}, {self.apellido}'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True
# Generated by Django 4.1 on 2022-10-31 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=50, verbose_name='Apellido')),
                ('email', models.CharField(max_length=100, unique=True, verbose_name='Email')),
                ('fecha_alta', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de registro')),
                ('ultimo_login', models.DateTimeField(auto_now_add=True, verbose_name='Ultimo login')),
                ('is_admin', models.BooleanField(default=True, verbose_name='Administrador')),
                ('is_staff', models.BooleanField(default=True, verbose_name='Staff')),
                ('is_active', models.BooleanField(default=True, verbose_name='Activo')),
                ('is_superadmin', models.BooleanField(default=True, verbose_name='Superadmin')),
            ],
            options={
                'verbose_name': 'Cuenta de Usuario',
                'verbose_name_plural': 'Cuentas de Usuarios',
                'ordering': ['fecha_alta'],
            },
        ),
    ]

# Generated by Django 4.1 on 2022-10-21 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=50, verbose_name='Apellido')),
                ('email', models.CharField(max_length=100, unique=True, verbose_name='Email')),
                ('password', models.CharField(max_length=50, verbose_name='Contraseña')),
                ('fecha_alta', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Alta')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'ordering': ['-fecha_alta'],
            },
        ),
    ]
# Generated by Django 2.0.2 on 2019-12-09 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190415_0657'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='avatar',
        ),
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Direccion'),
        ),
        migrations.AddField(
            model_name='profile',
            name='birthdate',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Fecha de Nacimiento'),
        ),
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Ciudad'),
        ),
        migrations.AddField(
            model_name='profile',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Pais'),
        ),
        migrations.AddField(
            model_name='profile',
            name='district',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Distrito'),
        ),
        migrations.AddField(
            model_name='profile',
            name='document',
            field=models.IntegerField(blank=True, choices=[(1, 'DNI'), (2, 'CE'), (3, 'Pasaporte')], null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='document_number',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Numero de Documento'),
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Correo Electronico'),
        ),
        migrations.AddField(
            model_name='profile',
            name='occupation',
            field=models.IntegerField(blank=True, choices=[(1, 'Ama de Casa'), (2, 'Desempleado(a)'), (3, 'Empleado'), (4, 'Empleador(a)'), (5, 'Estudiante'), (6, 'Jubilado(a)'), (7, 'Miembro de las Fuerzas Armadas'), (8, 'Obrero'), (9, 'Trabajador(a) del Hogar'), (10, 'Trabajador(a) Independiente'), (11, 'No declara')], null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='Telefono'),
        ),
    ]

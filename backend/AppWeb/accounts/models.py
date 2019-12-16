from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _
from .helpers import profile_image_path

DOCUMENT_TYPE = (
    (1, 'DNI'),
    (2, 'CE'),
    (3, 'Pasaporte'),
)
OCCUPATION_TYPE = (
    (1, 'Ama de Casa'),
    (2, 'Desempleado(a)'),
    (3, 'Empleado'),
    (4, 'Empleador(a)'),
    (5, 'Estudiante'),
    (6, 'Jubilado(a)'),
    (7, 'Miembro de las Fuerzas Armadas'),
    (8, 'Obrero'),
    (9, 'Trabajador(a) del Hogar'),
    (10, 'Trabajador(a) Independiente'),
    (11, 'No declara'),
)                                                                                                                                                                                                                                                                                                                                                   
class Profile(models.Model):                                                                                        
    """An extension of user model."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    document = models.IntegerField(choices=DOCUMENT_TYPE, blank=True, null=True)
    document_number = models.CharField('Numero de Documento', max_length = 20, blank=True, null=True)
    phone = models.CharField(_('Telefono'), max_length=12, blank=True, null=True)
    email = models.CharField('Correo Electronico', max_length = 20, blank=True, null=True)
    birthdate = models.CharField('Fecha de Nacimiento (DD/MM/YYYY)', max_length = 15, blank=True, null=True)
    country = models.CharField('Pais', max_length = 100, blank=True, null=True)
    city = models.CharField('Ciudad', max_length = 100, blank=True, null=True)
    district = models.CharField('Distrito', max_length = 100, blank=True, null=True)
    address = models.CharField('Direccion', max_length = 150, blank=True, null=True)
    occupation = models.IntegerField('Ocupacion', choices=OCCUPATION_TYPE, blank=True, null=True)

    #created_at = models.DateTimeField(auto_now_add=True)
    #updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return username's name."""
        return f'{self.user.username} profile'


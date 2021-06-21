from typing import AbstractSet
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from SystemConfig.settings import MEDIA_URL, STATIC_URL

# Create your models here.
class User(AbstractUser):
    # Se agregan los campos que se necesiten al crear un nuevo usuario
    # (ver los campos por defecto en la base de datos...)
    is_admin = models.BooleanField(default=False)
    is_conta = models.BooleanField(default=False)
    is_comer = models.BooleanField(default=False)
    is_oper = models.BooleanField(default=False)
    is_tester = models.BooleanField(default=False)
    image = models.ImageField(upload_to='users/%Y/%m/%d', blank=True, null=True)
    
    # Método para obtener la ruta absoluta de la imagen
    
    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'main/img/empty.png')
    
# Para implementar la auditoría en los modelos, esto es: quien/cuando/que hizo cada usuario en la BD
# Se crea un modelo 'base' que tendrá los campos requeridos para cada modelo
from django.db import models
from SystemConfig.settings import AUTH_USER_MODEL

class BaseModel(models.Model):
    user_creation = models.ForeignKey(AUTH_USER_MODEL, related_name='user_creation', on_delete=models.CASCADE, blank=True, null=True)
    date_creation = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    user_updated = models.ForeignKey(AUTH_USER_MODEL, related_name='user_updated', on_delete=models.CASCADE, blank=True, null=True)
    date_updated = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        pass

    class Meta:
        abstract = True # Esta entidad no se creará en la DB, solo será usada por otras entidades
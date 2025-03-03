from django.db import models

# Create your models here.
class Zapatos(models.Model):  #nombre de la tabla en la Base de Datos
    nombre = models.CharField(max_length=100, default='DEFAULT VALUE')
    precio = models.CharField(max_length=20, default='DEFAULT VALUE')
    talla = models.IntegerField(default=0)  # Representa el número del zapato
    #stock = models.TextChoices('Si Hay', 'No hay')
    stock = models.CharField(max_length=100, default='DEFAULT VALUE')
    img = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Meta:
     db_table = 'zapatos' #nombre de instancia con la que llamamos la tabla en la Base de Datos
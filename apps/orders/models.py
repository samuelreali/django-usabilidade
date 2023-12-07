from django.db import models
from users.models import Users

# Create your models here.
class Order(models.Model):
    price = models.DecimalField('Preco', default=0, max_digits=10, decimal_places=2)
    #produto
    
    class Meta:
        verbose_name = 'Ordem'
        verbose_name_plural = 'Ordens'
        ordering =['id']

    def __str__(self):
        return self.name
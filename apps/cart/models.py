from django.db import models
# from user.models import User 

# Create your models here.
class Cart(models.Model):
    name = models.CharField('Nome do Cliente', max_length=50)
    date_order = models.DateField('Data do Pedido', auto_now=False, auto_now_add=False) 
    delivery = models.BooleanField('Ativo', default=False)
    
    class Meta:
        verbose_name = 'Carrinho'
        verbose_name_plural = 'Carrinhos'
        ordering =['id']

    def __str__(self):
        return self.name

from django.db import models
from categories.models import Category

# Create your models here.
class Product(models.Model):
    name = models.CharField('Nome', max_length=50)
    is_active = models.BooleanField('Ativo', default=False)
    is_cart = models.BooleanField('Carrinho', default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField('Preco', max_digits=10, decimal_places=2)
    
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering =['id']

    def __str__(self):
        return self.name
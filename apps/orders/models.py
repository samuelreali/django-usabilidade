from django.db import models

# Create your models here.
class Order(models.Model):
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descricao', max_length=100)
    #produto
    
    class Meta:
        verbose_name = 'Ordem'
        verbose_name_plural = 'Ordens'
        ordering =['id']

    def __str__(self):
        return self.name
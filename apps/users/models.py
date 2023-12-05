from django.db import models
from django.contrib.auth.hashers import make_password

class Users(models.Model):
    PROFILE_CHOICES = (
        ("a","Administrador"),
        ("c","Cliente")
    ) 
    name = models.CharField('Nome', max_length=50)
    phone = models.IntegerField('Telefone', unique=True)
    address = models.CharField('Endereco', max_length=50)
    email = models.CharField('Email', max_length=50, unique=True)
    password = models.CharField('Senha', max_length=128,null=False,default=phone)
    profile = models.CharField(max_length=1, choices=PROFILE_CHOICES, blank=False, null=False,default="c")
    class Meta:
        verbose_name = 'Users'
        verbose_name_plural = 'Users'
        ordering =['id']
    def __str__(self):
        return self.email

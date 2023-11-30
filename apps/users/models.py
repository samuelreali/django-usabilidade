from django.db import models
from django.contrib.auth.hashers import make_password

class Users(models.Model):
    name = models.CharField('Nome', max_length=50)
    phone = models.IntegerField('Telefone', max_length=18, unique=True)
    address = models.CharField('Endereco', max_length=50)
    email = models.CharField('Email', max_length=50, unique=True)
    password = models.CharField('Senha', max_length=128)  # Use um campo maior para armazenar o hash

    class Meta:
        verbose_name = 'Users'
        verbose_name_plural = 'Users'
        ordering =['id']

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        # Antes de salvar, criptografa a senha usando make_password
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

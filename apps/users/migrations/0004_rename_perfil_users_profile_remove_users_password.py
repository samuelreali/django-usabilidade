# Generated by Django 4.1 on 2023-12-04 22:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_users_perfil'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='perfil',
            new_name='profile',
        ),
        migrations.RemoveField(
            model_name='users',
            name='password',
        ),
    ]

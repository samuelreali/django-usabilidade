# Generated by Django 4.1 on 2023-12-07 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_remove_product_date_fabrication'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_cart',
            field=models.BooleanField(default=False, verbose_name='Carrinho'),
        ),
    ]

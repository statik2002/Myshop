# Generated by Django 5.0.4 on 2024-05-21 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0048_alter_product_linked_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='linked_products',
            field=models.ManyToManyField(blank=True, to='main.product', verbose_name='Связанные товары'),
        ),
    ]

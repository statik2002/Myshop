# Generated by Django 5.0.4 on 2024-04-26 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0037_alter_product_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='first_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Закупочная цена'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Розничная цена'),
        ),
    ]
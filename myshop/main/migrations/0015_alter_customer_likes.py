# Generated by Django 5.0 on 2024-01-23 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_remove_metrics_product_delete_color_delete_metrics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='likes',
            field=models.ManyToManyField(blank=True, null=True, to='main.product', verbose_name='Лайкнутые товары'),
        ),
    ]

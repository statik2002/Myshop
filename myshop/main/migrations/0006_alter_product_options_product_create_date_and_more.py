# Generated by Django 5.0 on 2024-01-01 17:17

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_product_tags'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name', '-create_date', 'show_count'], 'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AddField(
            model_name='product',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='metrics',
            name='height',
            field=models.DecimalField(decimal_places=3, max_digits=5, verbose_name='Высота см'),
        ),
        migrations.AlterField(
            model_name='metrics',
            name='length',
            field=models.DecimalField(decimal_places=3, max_digits=5, verbose_name='Длинна см'),
        ),
        migrations.AlterField(
            model_name='metrics',
            name='weight',
            field=models.DecimalField(decimal_places=3, max_digits=6, verbose_name='Вес кг'),
        ),
        migrations.AlterField(
            model_name='metrics',
            name='width',
            field=models.DecimalField(decimal_places=3, max_digits=5, verbose_name='Ширина см'),
        ),
    ]

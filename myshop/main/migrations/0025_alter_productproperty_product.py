# Generated by Django 5.0 on 2024-03-29 12:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_remove_productproperty_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productproperty',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='properties', to='main.product', verbose_name='Товар'),
        ),
    ]
# Generated by Django 5.0.3 on 2024-04-10 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0032_alter_catalog_code_1c'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='code_1c',
            field=models.PositiveIntegerField(unique=True, verbose_name='Код из 1С'),
        ),
    ]

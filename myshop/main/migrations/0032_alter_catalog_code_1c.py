# Generated by Django 5.0.3 on 2024-04-10 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_customer_pickpoint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='code_1c',
            field=models.PositiveIntegerField(unique=True, verbose_name='Код каталога из 1С'),
        ),
    ]
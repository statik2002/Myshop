# Generated by Django 5.0.3 on 2024-03-22 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_productproperty_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='production_origin',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Страна производитель'),
        ),
    ]

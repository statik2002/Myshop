# Generated by Django 5.0 on 2024-02-02 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_remove_productproperty_code_1c_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to='product_images', verbose_name='Изображение'),
        ),
    ]
# Generated by Django 5.0 on 2024-01-15 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_remove_product_code_1c_productproperty_code_1c'),
    ]

    operations = [
        migrations.AddField(
            model_name='productproperty',
            name='image',
            field=models.ImageField(default=0, upload_to='media/products/'),
            preserve_default=False,
        ),
    ]

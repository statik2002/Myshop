# Generated by Django 5.0 on 2024-03-06 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_product_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='likes',
        ),
    ]

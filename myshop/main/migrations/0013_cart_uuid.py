# Generated by Django 5.0 on 2024-03-23 04:12

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_product_production_origin'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]

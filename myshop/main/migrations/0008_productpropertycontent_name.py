# Generated by Django 5.0 on 2023-12-31 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_color_weight_productpropertycontent'),
    ]

    operations = [
        migrations.AddField(
            model_name='productpropertycontent',
            name='name',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]

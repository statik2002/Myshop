# Generated by Django 5.0.3 on 2024-03-27 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_alter_productproperty_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productproperty',
            name='color',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Color'),
        ),
    ]

# Generated by Django 5.0.4 on 2024-04-25 13:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0034_mainmenuitem_submenuitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submenuitem',
            name='menu_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submen', to='main.mainmenuitem'),
        ),
    ]

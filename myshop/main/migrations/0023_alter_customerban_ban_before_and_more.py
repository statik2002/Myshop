# Generated by Django 5.0 on 2024-02-18 13:03

import datetime
import main.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_alter_customerban_ban_before_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerban',
            name='ban_before',
            field=models.DateTimeField(default=main.models.CustomerBan.ban_delta, verbose_name='Бан до:'),
        ),
        migrations.AlterField(
            model_name='customerban',
            name='ban_datetime',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 18, 13, 3, 27, 643308, tzinfo=datetime.timezone.utc), verbose_name='Время бана'),
        ),
    ]
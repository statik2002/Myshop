# Generated by Django 5.0 on 2024-02-19 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_alter_customerban_ban_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='ban_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Время бана'),
        ),
    ]
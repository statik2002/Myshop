# Generated by Django 5.0 on 2024-03-01 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0044_alter_customer_email'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customer',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='customer',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='user_permissions',
        ),
        migrations.AddField(
            model_name='customer',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='is_active'),
        ),
    ]
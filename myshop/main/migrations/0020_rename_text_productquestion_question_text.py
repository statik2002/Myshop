# Generated by Django 5.0 on 2024-03-27 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_productquestion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productquestion',
            old_name='text',
            new_name='question_text',
        ),
    ]

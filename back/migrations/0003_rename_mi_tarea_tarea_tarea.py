# Generated by Django 5.0.6 on 2024-05-26 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0002_rename_tarea_tarea_mi_tarea'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tarea',
            old_name='mi_tarea',
            new_name='tarea',
        ),
    ]

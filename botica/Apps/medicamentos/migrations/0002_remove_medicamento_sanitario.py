# Generated by Django 3.0.8 on 2020-08-04 04:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicamentos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicamento',
            name='sanitario',
        ),
    ]

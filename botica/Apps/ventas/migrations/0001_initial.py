# Generated by Django 3.0.8 on 2020-07-22 05:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0001_initial'),
        ('medicamentos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cabecera_Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ruc', models.CharField(max_length=11, unique=True)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clientes.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='todo_item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(max_length=9)),
                ('list_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ventas.Cabecera_Venta')),
                ('medicamento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='medicamentos.Medicamento')),
            ],
        ),
    ]
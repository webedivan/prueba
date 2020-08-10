# Generated by Django 3.0.8 on 2020-07-21 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Presentacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lote', models.CharField(default=0, max_length=10, unique=True)),
                ('tipo', models.CharField(choices=[('Generico', 'generico'), ('Comercial', 'comercial')], max_length=30)),
                ('nombre', models.CharField(max_length=200, unique=True)),
                ('componente', models.CharField(max_length=200)),
                ('concentracion', models.CharField(max_length=50)),
                ('sanitario', models.CharField(max_length=190)),
                ('fecha_expiracion', models.DateField()),
                ('fecha_produccion', models.DateField()),
                ('descripcion', models.TextField(max_length=400)),
                ('precio_compra', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('precio_venta', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('stock', models.PositiveSmallIntegerField()),
                ('igv', models.DecimalField(decimal_places=2, default=0.0, max_digits=6)),
                ('presentacion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='medicamentos.Presentacion')),
            ],
        ),
    ]
# Generated by Django 3.0.8 on 2020-07-23 04:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('medicamentos', '0001_initial'),
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serie', models.IntegerField()),
                ('numero', models.CharField(max_length=6)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='clientes.cliente')),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('serie', 'numero')},
            },
        ),
        migrations.CreateModel(
            name='DetalleFactura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=40)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=6)),
                ('cantidad', models.IntegerField()),
                ('impuesto', models.DecimalField(decimal_places=2, max_digits=6)),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=6)),
                ('factura', models.ForeignKey(db_column='factura_id', on_delete=django.db.models.deletion.PROTECT, related_name='factura', to='factura.Factura')),
                ('producto', models.ForeignKey(db_column='medicamento_id', on_delete=django.db.models.deletion.PROTECT, to='medicamentos.Medicamento')),
            ],
        ),
    ]
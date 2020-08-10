from django.db import models
import  datetime
TAX_VALUE =0.18
# Create your models here.
class Presentacion(models.Model):
    nombre = models.CharField(max_length=60)
    def __str__(self):
        return f'{self.nombre}'
class Medicamento(models.Model):
    TIPO =(
        ('Generico','generico'),
        ('Comercial','comercial'),
          )
    lote =models.CharField(max_length=10,unique=True,default=0)
    presentacion =models.ForeignKey(Presentacion,on_delete=models.PROTECT)
    tipo = models.CharField(choices=TIPO,max_length=30)
    nombre = models.CharField(max_length=200, unique=True)
    componente = models.CharField(max_length=200)
    concentracion = models.CharField(max_length=50)
    fecha_expiracion = models.DateField()
    fecha_produccion = models.DateField()
    descripcion = models.TextField(max_length=400)
    precio_compra = models.DecimalField(max_digits=5,decimal_places=2,default=0.00)
    precio_venta = models.DecimalField(max_digits=5,decimal_places=2, default=0.00)
    stock =models.PositiveSmallIntegerField()
    igv = models.DecimalField(max_digits=6,decimal_places=2,default=0.00)
    def __str__(self):
        return f'{self.nombre}'

    def preciototal(self):
        precio_total =self.precio_compra*self.stock
        return precio_total

    def stadomedicamento(self):
        hoy = datetime.date.today()
        dias = (self.fecha_expiracion-hoy).days
        return  dias
    def incrementarlote(self,*args,**kwargs):
        if self.lote == 0:
            self.lote +=1
            self.store.save()
        super (Medicamento,self).save(*args,**kwargs)

    def save(self,*args,**kwargs):
        if self.precio_venta:
            self.igv = round(float(self.precio_venta)*TAX_VALUE,3)
            super(Medicamento, self).save(*args,**kwargs)
        else:
            self.igv=0
            super(Medicamento, self).save(*args,**kwargs)
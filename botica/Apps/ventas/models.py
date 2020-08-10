from django.db.models import signals
from django.db import models
from  botica.Apps.clientes.models import cliente
from  botica.Apps.medicamentos.models import Medicamento
# Create your models here.
class Cabecera_Venta(models.Model):
    cliente = models.ForeignKey(cliente,on_delete=models.PROTECT)
    fecha = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.ruc}'

class todo_item(models.Model):
    list_id = models.ForeignKey(Cabecera_Venta,on_delete=models.PROTECT)
    medicamento = models.ForeignKey(Medicamento,on_delete=models.PROTECT)
    cantidad = models.IntegerField()

def update_stock(sender, instance, **kwargs):
    instance.medicamento.stock -= instance.cantidad
    instance.medicamento.save()
signals.post_save.connect(update_stock, sender=todo_item, dispatch_uid="update_stock_count")
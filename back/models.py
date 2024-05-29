from django.db import models


class Tarea(models.Model):
    tarea = models.CharField(max_length=200, help_text='Tarea a realizar.')
    creado = models.DateTimeField(auto_now_add=True, help_text='Fecha de creación.')
    vencimiento = models.DateTimeField(null=True, blank=True, help_text='Fecha de vencimiento.')

    def __str__(self):
        return self.tarea

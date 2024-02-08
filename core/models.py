from django.db import models

# Create your models here.
class Plan(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    updated = models.DateTimeField(auto_now_add=True,blank=True, null=True)

    def __str__(self):
        return (f"{self.nombre} | {self.descripcion} | {self.precio}") 
    def Meta(self):
        verbose_name = 'Plan'
        verbose_name_plural = 'Planes'
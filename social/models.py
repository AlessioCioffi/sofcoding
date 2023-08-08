from django.db import models

# Create your models here.
class Social(models.Model):
    
    name = models.CharField(verbose_name='Nombre',max_length=200)
    link = models.URLField(verbose_name='Enlace', null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de edición")
    
    class Meta:
        verbose_name = "Enlace"
        verbose_name_plural = "Redes Sociales"
        ordering = ["name"]
        
    def __str__(self):
        return self.name
    
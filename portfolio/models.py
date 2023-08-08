from django.db import models

# Create your models here.
class Project(models.Model):
    
    title = models.CharField(max_length=200,verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imagen",upload_to="project",null=True,blank=True)
    link = models.URLField(null=True,blank=True,verbose_name="Dirección Web")    
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de edición")
    order_number = models.IntegerField(default=0, verbose_name="Numero")
    
    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["order_number"]
        ''' clase para que podamos cambiar los nombre 
        y ordenar los proyecto como queremos'''
    #__str__ returnamos la informacion que elegimos
    def __str__(self):
        return self.title

#cada vez que creamos un model es necesario el makemigration y migrate



from django.contrib import admin
from .models import Project
# Register your models here.
'''la clase ProjectAdmin la creo para que en el panel de admin
encontremos la el created y update que por defecto no aparecen
porque son campos que se crean automáticamente'''
class ProjectAdmin(admin.ModelAdmin):
    
    readonly_fields = ("created","updated")

#linea de codigo para que en el panel admin se refleja el modelo
admin.site.register(Project,ProjectAdmin)
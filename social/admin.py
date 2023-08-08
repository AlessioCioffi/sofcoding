from django.contrib import admin
from .models import Social
# Register your models here.

class SocialAdmin(admin.ModelAdmin):
    
    readonly_fields = ("created","updated")

#linea de codigo para que en el panel admin se refleja el modelo
admin.site.register(Social,SocialAdmin)

# Register your models here.

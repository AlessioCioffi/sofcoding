from django.shortcuts import render
from .models import Project
# Create your views here.
def portfolio(request):
    projects = Project.objects.all()
    '''En esta vista recibimos la request portfolio;
       a esta peticion le devolvemos el template y
       en la variable project estamos llamando con el 
       atributo object.all() todos los items que que contiene
       el modelo Project. Ahroa tenemos que iñetar la lista de
       projects al template y lo hacemos creando un tercer parametro
       con un dicionario "de contesto" con una llave a la qual le asiñamos
       el valor que en este caso es la variable projects'''
    return render(request,"portfolio/project.html",{'progetti':projects})
    
def project(request,id):
   project = Project.objects.get(id=id)
   return render(request,"portfolio/detail.html",{'proyecto':project})
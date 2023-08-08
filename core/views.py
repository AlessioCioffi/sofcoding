from django.shortcuts import render

html_base = """

<h1>Mi web personal<h1>
<ul> 
    <li><a href="/">Portada</a></li>
    <li><a href="/about-me/">Acerca de</a></li>
    <li><a href="/portfolio/">Portfolio</a></li>
    <li><a href="/contact/">Contacto</a></li>
    
    """
# Create your views here.
def home(request):
    return render(request,"core/home.html")

def about(request):
    return render(request,"core/about-me.html")
    
def contact(request):
    return render(request,"core/contact.html")

                        
                        
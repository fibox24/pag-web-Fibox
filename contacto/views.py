from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import FormularioContacto
# Create your views here.
def Contacto(request):
    
    if request.method == 'POST':
        miFormulario=FormularioContacto(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            send_mail(informacion['asunto'], informacion['nombre'] + " con email: " + informacion['email'] + " dice: " + informacion['mensaje'], informacion.get('email',''),['fibox.adm@gmail.com'],)

            return render(request, 'core/mensaje_enviado.html')
    else:
        miFormulario=FormularioContacto()

    return render(request, 'core/contacto.html', {'miFormulario':miFormulario})

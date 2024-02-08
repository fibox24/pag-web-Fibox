from django import forms

class FormularioContacto(forms.Form):
    nombre = forms.CharField(label="Nombre")
    email = forms.EmailField(label="Correo electrónico")
    asunto = forms.CharField(label="Asunto")
    mensaje = forms.CharField(label="Mensaje", widget=forms.Textarea)
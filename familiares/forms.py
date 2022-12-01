from django import forms


class PersonaForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    edad = forms.IntegerField()
    fecha_nacimiento = forms.DateField()
    
    
class PaqueteForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    peso = forms.IntegerField()
    remitente = forms.CharField(max_length=50)
    destinatario = forms.CharField(max_length=50)

class CelularForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    modelo = forms.CharField(max_length=50)
    marca = forms.CharField(max_length=50)
    fecha_lanzamiento = forms.DateField()

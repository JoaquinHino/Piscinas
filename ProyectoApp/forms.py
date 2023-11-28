from django import forms
from .models import Usuario, Mensaje


# forms.py
from django import forms

class LoginForm(forms.Form):
    correo = forms.EmailField(label='Correo electrónico')
    contrasena = forms.CharField(widget=forms.PasswordInput, label='Contraseña')

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'correo', 'password']

class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['nombre', 'apellido', 'correo', 'mensaje']
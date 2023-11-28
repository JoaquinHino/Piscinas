from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegistroForm, MensajeForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib import messages

                                                                                                                           

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            correo = form.cleaned_data['correo']
            contrasena = form.cleaned_data['contrasena']

            # Imprimir para depuración
            print(f"Correo: {correo}")
            print(f"Contraseña: {contrasena}")

            user = authenticate(request, username=correo, password=contrasena)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                form.add_error(None, 'Credenciales incorrectas. Inténtalo de nuevo.')
    else:
        form = LoginForm()

    return render(request, 'templatesApp/login.html', {'form': form})

def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.password = make_password(form.cleaned_data['password'])
            usuario.save()
            return redirect('templatesApp/index.html')  # Redirige a la página de éxito
    else:
        form = RegistroForm()

    return render(request, 'templatesApp/registro.html', {'form': form})



def contacto_view(request):
    mensaje_enviado = None

    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            form.save()
            mensaje_enviado = "¡Mensaje enviado con éxito!"
            messages.success(request, mensaje_enviado)  # Añade este mensaje de éxito
    else:
        form = MensajeForm()

    return render(request, 'templatesApp/contact.html', {'form': form, 'mensaje_enviado': mensaje_enviado})


def registro_exitoso(request):
    return render(request, 'templatesApp/registro_exitoso.html')



def renderTemplate3(request):
    return render(request,'templatesApp/index.html')

def renderTemplate4(request):
    return render(request,'templatesApp/shop.html')

def renderTemplate5(request):
    return render(request,'templatesApp/cart.html')

def renderTemplate6(request):
    return render(request,'templatesApp/contact.html')

def renderTemplate7(request):
    return render(request,'templatesApp/login.html')

def renderTemplate8(request):
    return render(request,'templatesApp/checkout.html')
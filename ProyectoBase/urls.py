"""ProyectoBase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ProyectoApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.renderTemplate3, name='index'),
    path('shop/', views.renderTemplate4, name='shop'),
    path('cart/', views.renderTemplate5, name='cart'),
    path('contact/', views.contacto_view, name='contacto_view'),
    path('login/', views.login_view, name='login'),
    path('checkout/', views.renderTemplate8, name='checkout'),
    path('registro/', views.registro_view, name='registro'),
    path('registro_exitoso/', views.registro_exitoso, name='registro_exitoso'),
]

from django.shortcuts import render

# Create your views here.

from .models import Zapatos

#Instanciamos las vistas genéricas de Django

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

#Nos sirve para redireccionar despues de una acción revertiendo patrones de expresiones regulares

from django.urls import reverse
#Habilitamos el uso de mensajes en Django

from django.contrib import messages
#Habilitamos los mensajes para class-based views

from django.contrib.messages.views import SuccessMessageMixin
#Habilitamos los formularios en Django

from django import forms

class ZapatoListado(ListView):
    model = Zapatos # Llamamos a la clase 'Zapato' que se encuentra en nuestro archivo 'models.py' 

class ZapatoCrear(SuccessMessageMixin, CreateView): 
    model = Zapatos # Llamamos a la clase 'Zapato' que se encuentra en nuestro archivo 'models.py'
    form = Zapatos # Definimos nuestro formulario con el nombre de la clase o modelo 'Zapatos'
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Zapatos' de nuestra Base de Datos 
    success_message = 'Zapatos Creada Correctamente!' # Mostramos este Mensaje luego de Crear una Zapatos

    # Redireccionamos a la página principal luego de crear un registro o Zapatos
    def get_success_url(self):        
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
    
class ZapatoDetalle(DetailView): 
    model = Zapatos # Llamamos a la clase 'Zapatos' que se encuentra en nuestro archivo 'models.py' 

class ZapatoActualizar(SuccessMessageMixin, UpdateView): 
    model = Zapatos # Llamamos a la clase 'Zapatos' que se encuentra en nuestro archivo 'models.py' 
    form = Zapatos # Definimos nuestro formulario con el nombre de la clase o modelo 'Zapatos' 
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Zapatos' de nuestra Base de Datos 
    success_message = 'Zapatos Actualizada Correctamente !' # Mostramos este Mensaje luego de Editar un Zapatos 

    # Redireccionamos a la página principal luego de actualizar un registro o Zapatos
    def get_success_url(self):               
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
    
class ZapatoEliminar(SuccessMessageMixin, DeleteView): 
    model = Zapatos 
    form = Zapatos
    fields = "__all__"     

    # Redireccionamos a la página principal luego de eliminar un registro o Zapatos
    def get_success_url(self): 
        success_message = 'Zapatos Eliminada Correctamente !' # Mostramos este Mensaje luego de Editar una Zapatos 
        messages.success (self.request, (success_message))       
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
    
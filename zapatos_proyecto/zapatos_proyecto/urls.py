"""
URL configuration for zapatos_proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from  zapatos_app.views import ZapatoListado, ZapatoDetalle, ZapatoCrear, ZapatoActualizar, ZapatoEliminar


urlpatterns = [

    path('admin/', admin.site.urls),

    # La ruta 'leer' en donde listamos todos los registros o zapatos de la Base de Datos
    path('zapatos/', ZapatoListado.as_view(template_name = "zapatos/index.html"), name='leer'),

    # La ruta 'detalles' en donde mostraremos una página con los detalles de un zapatos o registro 
    path('zapatos/detalle/<int:pk>', ZapatoDetalle.as_view(template_name = "zapatos/detalles.html"), name='detalles'),

    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo zapatos o registro  
    path('zapatos/crear', ZapatoCrear.as_view(template_name = "zapatos/crear.html"), name='crear'),

    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un zapatos o registro de la Base de Datos 
    path('zapatos/editar/<int:pk>', ZapatoActualizar.as_view(template_name = "zapatos/actualizar.html"), name='actualizar'), 

    # La ruta 'eliminar' que usaremos para eliminar un zapatos o registro de la Base de Datos 
    path('zapatos/eliminar/<int:pk>', ZapatoEliminar.as_view(), name='eliminar'),   
]
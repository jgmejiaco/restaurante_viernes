from django.shortcuts import render

from web.formularios.formularioPlatos import FormularioRegistroPlatos
from web.formularios.formularioEmpleados import FormularioRegistroEmpleados

from web.models import Platos
from web.models import Empleados

# Create your views here.
#cada vista es una función de Python, este archivo se encarga de renderizar el contenido HTML y subirlo al DOM

def Home(request):
    return render(request, 'index.html')

def PlatosVista(request):

    #cargar el formulario de registro de platos
    formulario=FormularioRegistroPlatos()

    #creamos un diccionario para enviar datos hacia el template
    diccionarioEnvioDatos={
        'formulario':formulario
    }

    #recibiendo datos del formulario "petición tipo POST"
    if request.method=='POST':
        datosFormulario=FormularioRegistroPlatos(request.POST)
        if datosFormulario.is_valid():
            datosLimpios=datosFormulario.cleaned_data
            #ENVIANDO DATOS A LAS BD
            platoNuevo=Platos(
                nombre=datosLimpios["nombrePlato"],
                descripcion=datosLimpios["descripcionPlato"],
                imagen=datosLimpios["fotoPlato"],
                precio=datosLimpios["precioPlato"],
                tipo=datosLimpios["tipoPlato"]
            )
            platoNuevo.save()

    return render(request, 'platos.html', diccionarioEnvioDatos)

def EmpleadosVista(request):
    #cargar el formulario de registro de platos
    formularioEmpleados=FormularioRegistroEmpleados()

    #creamos un diccionario para enviar datos hacia el template
    diccionarioEnvioDatos={
        'formularioEmpleados':formularioEmpleados
    }

    #recibiendo datos del formulario "petición tipo POST"
    if request.method=='POST':
        datosFormulario=FormularioRegistroEmpleados(request.POST)
        if datosFormulario.is_valid():
            datosLimpios=datosFormulario.cleaned_data

            #ENVIANDO DATOS A LAS BD
            empleadoNuevo=Empleados(
                nombres=datosLimpios["nombreEmpleado"],
                apellidos=datosLimpios["apellidoEmpleado"],
                foto=datosLimpios["fotoEmpleado"],
                documento=datosLimpios["documentoEmpleado"],
                tipo=datosLimpios["tipoEmpleado"]
            )

            empleadoNuevo.save()

    return render(request, 'empleados.html', diccionarioEnvioDatos)
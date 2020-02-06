from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from Nomina.models import Cargo
from Nomina.forms import CargosForm
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
PAGE_TITLE = "Empleados activos en la nomina"

def index(request):
    pass

def nuevo(request):
    pass

def detalles(request):
    pass

def editar(request, id_empleado):
    pass

def eliminar(request, id_empleado):
    pass

def list_json(request):
    pass
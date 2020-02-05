from django.http import JsonResponse
from django.shortcuts import render
from Nomina.models import Cargo


PAGE_TITLE = "Cargos para empleados"


def index(request):
    return render(request, 'Nomina/Cargos/index.html', {'titulo': PAGE_TITLE})


def list_json(request):
    lista_cargos = list(Cargo.objects.all().only("CodigoCargo", "Descripcion", "FechaCreacion"))
    return JsonResponse(data={"data": lista_cargos}, safe=True)


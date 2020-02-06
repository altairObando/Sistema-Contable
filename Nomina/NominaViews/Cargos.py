from django.http import JsonResponse
from django.shortcuts import render
from Nomina.models import Cargo
from Nomina.forms import CargosForm
PAGE_TITLE = "Cargos disponibles"


def index(request):
    return render(request, 'Nomina/Cargos/index.html', {'titulo': PAGE_TITLE})


def list_json(request):
    lista_cargos = list(Cargo.objects.all().values("CodigoCargo", "Descripcion", "FechaCreacion", "id"))

    return JsonResponse(data={"data": lista_cargos}, safe=True)

def nuevo_cargo(request):
    template= 'Nomina/Cargos/create.html'
    if request.method == "POST":
        form = CargosForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=false)
            instance.save()
            return JsonResponse({'guardado': True, 'mensaje': 'Cargo agregado'}, safe=False)
    else:
        form = CargosForm()
        return render(request, template, {'form': form, 'titulo': 'Crear nuevo cargo'})
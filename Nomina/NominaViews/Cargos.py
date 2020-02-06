from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from Nomina.models import Cargo
from Nomina.forms import CargosForm
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
PAGE_TITLE = "Cargos disponibles"


def index(request):
    return render(request, 'Nomina/Cargos/index.html', {'titulo': PAGE_TITLE})


def list_json(request):
    lista_cargos = list(Cargo.objects.all().values("CodigoCargo", "Descripcion", "FechaCreacion", "id"))
    return JsonResponse(data={"data": lista_cargos}, safe=True)


def nuevo_cargo(request):
    template = 'Nomina/Cargos/create.html'
    if request.method == "POST":
        form = CargosForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return JsonResponse({'guardado': True, 'mensaje': 'Cargo agregado'}, safe=False)
        else:
            return JsonResponse({'guardado': False, 'mensaje': 'No se pudo guardar el cargo'}, safe=False)
    else:
        form = CargosForm()
        return render(request, template, {'form': form})


def detalles_cargo(request, id_cargo):
    cargo = get_object_or_404(Cargo, pk=id_cargo)
    return render(request, 'Nomina/Cargos/details.html', {'model': cargo})


def editar_cargo(request, id_cargo):
    template = 'Nomina/Cargos/edit.html'
    cargo = get_object_or_404(Cargo, pk=id_cargo)
    if request.method == "POST":
        form = CargosForm(request.POST, instance=cargo)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return JsonResponse({'guardado': True, 'mensaje': 'Cargo actualizado'}, safe=False)
        else:
            return JsonResponse({'guardado': False, 'mensaje': 'No se pudo actualizar el cargo'}, safe=False)
    else:
        form = CargosForm(instance=cargo)
        return render(request, template, {
            'form': form,
            'cargos_edit_uri': reverse('cargos_edit', args=(id_cargo,))
        })


@csrf_exempt
def elimnar_cargo(request, id_cargo):
    if request.method == "POST":
        cargo = get_object_or_404(Cargo, pk=id_cargo)
        cargo.delete()
        return JsonResponse(data={"guardado": True, "message": "Se ha eliminado el cargo"}, safe=True)
    return JsonResponse(data={"guardado": False, "message": "Este metodo solo permite operaciones POST"}, safe=True)
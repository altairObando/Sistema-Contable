from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from Nomina.models import Empleado
from Nomina.forms import EmpleadosForm
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

PAGE_TITLE = "Empleados"


def index(request):
    return render(request, 'Nomina/Empleados/index.html', {'titulo': PAGE_TITLE})


def nuevo(request):
    if request.method == "POST":
        form = EmpleadosForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.Estado = True
            instance.save()
            return JsonResponse(data={"guardado": True, "message": "Se a registrado el nuevo empleado"}, safe=True)
        else:
            return JsonResponse(data={"guardado": False, "message": form.errors}, safe=True)
    else:
        form = EmpleadosForm()
        return render(request, 'Nomina/Empleados/create.html', {'form': form})


def detalles(request, id_empleado):
    empleado = get_object_or_404(Empleado, pk=id_empleado)
    return render(request, 'Nomina/Empleados/details.html', {'data': empleado})


def editar(request, id_empleado):
    empleado = get_object_or_404(Empleado, pk=id_empleado)
    if request.method == "POST":
        form = EmpleadosForm(request.POST, instance=empleado)
        if form.is_valid():
            result = form.save(commit=False)
            result.Estado = True
            result.save()
            return JsonResponse(data={"guardado": True, "message": "Se a registrado el nuevo empleado"}, safe=True)
        else:
            return JsonResponse(data={"guardado": False, "message": form.errors}, safe=True)
    else:
        form = EmpleadosForm(instance=empleado)
        return render(request, 'Nomina/Empleados/edit.html', {'form': form, 'form_url': reverse('edit_empleados', args=(id_empleado,))})


def list_json(request):
    lista = Empleado.objects.filter(Estado=True).values("Cedula", "NoInss", "Nombres", "PrimerApellido",
                                                        "SegundoApellido", "GradoAcademico", "id")
    return JsonResponse(data={"data": list(lista)}, safe=True)


@csrf_exempt
def eliminar(request, id_empleado):
    if request.method == "POST":
        empleado = get_object_or_404(Empleado, pk=id_empleado)
        empleado.Estado = False  # Eliminacion logica
        empleado.save()
        return JsonResponse(data={"Guardado": True, 'message': "Empleado eliminado"})
    return JsonResponse(data={"Guardado": False, 'message': "Metodo no admitido"})
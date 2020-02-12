from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from Nomina.models import Empleado, Cargo,  FotosEmpleado, EmpleadoCargo
from Nomina.forms import EmpleadosForm, EmpleadoFotoForm
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
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


def agregar_foto(request, id_empleado):
    if request.method == "POST":
        form = EmpleadoFotoForm(request.POST, request.FILES)
        if form.is_valid():
            FotosEmpleado.objects.filter(Empleado_id=id_empleado).update(Activa=False)
            foto = form.files["id_Foto"]
            emp = Empleado.objects.get(pk=id_empleado)
            data = FotosEmpleado()
            data.Foto = foto
            data.Empleado = emp
            data.Empleado_id = id_empleado
            data.Fecha = datetime.now()
            data.Activa = True
            data.save()
            return JsonResponse(data={"Guardado": True, 'message': "Foto de empleado guardada"})
        else:
            return JsonResponse(data={"Guardado": False, 'message': "No se ha cargado la foto del empleado"})
    else:
        empleado = Empleado.objects.get(pk=id_empleado)
        actual = list(FotosEmpleado.objects.filter(Empleado__id=id_empleado, Activa=True))
        if len(actual) == 0:
            actual = None
        else:
            actual = actual[0]
        form = EmpleadoFotoForm()
        return render(request, 'Nomina/Empleados/add_photo.html', {
            'data': empleado,
            'form': form,
            'form_uri': reverse('add_photo_empleados', args=(id_empleado,)),
            'fotoActual': actual
        })

def asignar_cargo(request, id_empleado):
    if request.method == "POST":
        id_cargo = request["id_cargo"]
        emp = EmpleadoCargo()
        emp.Cargo_id = id_cargo
        emp.Empleado_id = id_empleado
        emp.save()
        return JsonResponse(data={"Guardado": True, 'message': "Cargo Actualizado"})
    else:
        cargos = Cargo.objects.all()
        return render(request,'Nomina/Empleados/add_cargo.html', {'cargos': cargos})


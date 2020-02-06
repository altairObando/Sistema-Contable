from django.urls import path
from Nomina.NominaViews import Empleado

urlpatterns = [
    path("", Empleado.index, name="index_empleados"),
    path("json/", Empleado.list_json, name="list_json_empleados"),
    path("DetallesEmpleado/<int:id_empleado>/", Empleado.detalles, name="details_empleados"),
    path("EditarEmpleado/<int:id_empleado>/", Empleado.editar, name="edit_empleados"),
    path("EliminarEmpleado/<int:id_empleado>/", Empleado.editar, name="edit_empleados"),
]
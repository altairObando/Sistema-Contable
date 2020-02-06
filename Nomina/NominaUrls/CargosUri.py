from django.urls import path
from Nomina.NominaViews import Cargos

urlpatterns = [
    path("", Cargos.index, name="cargos_index_view"),
    path('json/', Cargos.list_json, name="cargos_list_json"),
    path('NuevoCargo/', Cargos.nuevo_cargo, name="cargos_create"),
    path("DetallesCargo/<int:id_cargo>/", Cargos.detalles_cargo, name="cargos_details"),
    path('EditarCargo/<int:id_cargo>/', Cargos.editar_cargo, name="cargos_edit"),
    path('EliminarCargo/<int:id_cargo>/', Cargos.elimnar_cargo, name="cargos_delete"),
]
from django.urls import path
from Nomina.NominaViews import Cargos

urlpatterns = [
    path("", Cargos.index, name="cargos_index_view"),
    path('json/', Cargos.list_json, name="cargos_list_json"),
    path('NuevoCargo', Cargos.nuevo_cargo, name="cargos_create"),
]
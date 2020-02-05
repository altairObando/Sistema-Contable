from django.urls import path
from Nomina.NominaViews import Cargos

urlpatterns = [
    path("", Cargos.index, name="cargos_index_view"),
]
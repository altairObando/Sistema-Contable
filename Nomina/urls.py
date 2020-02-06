from django.urls import path, include

urlpatterns = [
    path('Cargos/', include("Nomina.NominaUrls.CargosUri")),
    path('Empleados/', include("Nomina.NominaUrls.EmpleadosUri")),
]
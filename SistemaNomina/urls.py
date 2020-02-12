
from django.contrib import admin
from django.urls import path, include
from SistemaNomina.views import index
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', index, name="index_page"),
    path('admin/', admin.site.urls),
    path('Nomina/', include("Nomina.urls"))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

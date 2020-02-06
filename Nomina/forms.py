from Nomina.models import Cargo
from django.forms import ModelForm

class CargosForm(ModelForm):
    class Meta:
        model = Cargo
        fields = "__all__"
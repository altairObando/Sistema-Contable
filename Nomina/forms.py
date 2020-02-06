from Nomina.models import Cargo
from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column


class DateInput(forms.DateInput):
    input_type = "date"

    def __init__(self, **kwargs):
        kwargs["format"] = "%d-%m-%Y"
        super().__init__(**kwargs)


class TimeInput(forms.TimeInput):
    input_type = "time"


class DateTimeInput(forms.DateTimeInput):
    input_type = "datetime-local"

    def __init__(self, **kwargs):
        kwargs["format"] = "%Y-%m-%dT%H:%M"
        super().__init__(**kwargs)


class CargosForm(ModelForm):
    class Meta:
        model = Cargo
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ##self.fields["FechaCreacion"].widget = DateInput()
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('FechaCreacion', css_class='form-group col-md-6 mb-0'),
                Column('CodigoCargo', css_class='form-group col-md-6 mb-0'),
                css_class="form-row"
            ), 'Descripcion',
            Submit('submit', 'Guardar cargo')
        )

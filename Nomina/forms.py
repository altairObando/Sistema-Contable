from Nomina.models import Cargo, Empleado
from django import forms
from django.forms import ModelForm, Textarea
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


class EmpleadosForm(ModelForm):
    class Meta:
        model = Empleado
        fields = "__all__"
        widgets: {
            'Direccion': Textarea(attrs={'rows': 3, 'cols': 10}),
            'Observaciones': Textarea(attrs={'rows': 3, 'cols': 10}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('Cedula', css_class='form-group col-md-4 mb-0'),
                Column('NoInss', css_class='form-group col-md-4 mb-0'),
                Column('CuentaBanco', css_class='form-group col-md-4 mb-0'),
            ),
            Row(
                Column('Nombres', css_class='form-group col-md-6 mb-0'),
                Column('PrimerApellido', css_class='form-group col-md-6 mb-0'),
            ),
            Row(
                Column('SegundoApellido', css_class='form-group col-md-6 mb-0'),
                Column('Email', css_class='form-group col-md-6 mb-0'),
            ),
            Row(
                Column('Sexo', css_class='form-group col-md-6 mb-0'),
                Column('EstadoCivil', css_class='form-group col-md-6 mb-0'),
            ),
            Row(
                Column('GradoAcademico', css_class='form-group col-md-6 mb-0'),
                Column('TipoEmpleado', css_class='form-group col-md-6 mb-0'),
            ), 'Direccion', 'Observaciones',
            Submit('submit', 'Guardar Empleado', css_class='btn btn-sm btn-success')
        )
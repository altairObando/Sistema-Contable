# Generated by Django 3.0.3 on 2020-02-07 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nomina', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cargo',
            name='FechaCreacion',
            field=models.DateField(auto_created=True, verbose_name='Fecha de creación'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='Cedula',
            field=models.CharField(max_length=17, verbose_name='Número de cédula'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='GradoAcademico',
            field=models.CharField(choices=[('1', 'Bachiller'), ('2', 'Tecnico'), ('3', 'Egresado'), ('4', 'Ingeniero'), ('5', 'Licenciatura'), ('6', 'Maestría'), ('7', 'Especialidad'), ('8', 'Doctorado')], max_length=1, verbose_name='Grado Academico'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='NoInss',
            field=models.IntegerField(blank=True, verbose_name='Número de INSS'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='TipoEmpleado',
            field=models.CharField(max_length=50, verbose_name='Tipo de Empleado'),
        ),
    ]

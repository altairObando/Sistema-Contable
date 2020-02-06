from django.db import models


class Empleado(models.Model):
    ESTADO_CIVIL = [
        ("1", "Soltero/a"),
        ("2", "Comprometido/a"),
        ("3", "En Relación"),
        ("4", "Casado/a"),
        ("5", "Unión libre"),
        ("6", "Separado/a"),
        ("7", "Viudo/a"),
    ]
    SEXO = [
        ("M", "Masculino"),
        ("F", "Femenino"),
        ("O", "Otro"),
    ]
    GRADO_ACADEMICO = [
        ("1", "Bachiller"),
        ("2", "Tecnico"),
        ("3", "Egresado"),
        ("4", "Ingeniero"),
        ("5", "Licenciatura"),
        ("6", "Maestría"),
        ("7", "Especialidad"),
        ("8", "Doctorado"),

    ]
    Cedula = models.CharField(max_length=15, verbose_name="Número de cédula")
    NoInss = models.IntegerField(verbose_name="Número de INSS")
    CuentaBanco = models.IntegerField(verbose_name="Número de cuenta bancaria", blank=True, null=True)
    Nombres = models.CharField(max_length=30)
    PrimerApellido = models.CharField(max_length=30, verbose_name="Primer apellido")
    SegundoApellido = models.CharField(max_length=25, verbose_name="Segundo apellido", blank=True, null=True)
    Sexo = models.CharField(max_length=1, choices=SEXO)
    EstadoCivil = models.CharField(max_length=1, choices=ESTADO_CIVIL)
    Email = models.EmailField(verbose_name="Correo Electrónico")
    Estado = models.BooleanField(verbose_name="Activo en el sistema", default=True)
    Direccion = models.TextField()
    TipoEmpleado = models.CharField(max_length=50)
    GradoAcademico = models.CharField(max_length=1, choices=GRADO_ACADEMICO)
    Observaciones = models.TextField(blank=True)

    def __str__(self):
        return "%s %s %s" % (self.Cedula, self.Nombres, self.PrimerApellido)


class FotosEmpleado(models.Model):
    Empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, verbose_name="Propietario")
    Foto = models.ImageField(verbose_name="Imagen Empleado", upload_to="EmpleadosImagen")
    Activa = models.BooleanField(verbose_name="Foto actual")
    Fecha = models.DateField(verbose_name="Fecha de creación")

    def __str__(self):
        return "%s %s" % (self.Empleado.PrimerApellido, self.Fecha)


class SalarioEmpleado(models.Model):
    Empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    FechaAsignacion = models.DateField(verbose_name="Fecha de asignación")
    Monto = models.DecimalField(max_digits=10, decimal_places=4)
    Activo = models.BooleanField(default=True, verbose_name="Salario activo")

    def __str__(self):
        return "%s %s" % (self.Empleado, str(self.Monto))


class Cargo(models.Model):
    CodigoCargo = models.CharField(max_length=10, verbose_name="Código de cargo")
    Descripcion = models.CharField(max_length=50)
    FechaCreacion = models.DateField(auto_created=True, verbose_name="Fecha de creación")

    def __str__(self):
        return "%s %s" % (self.CodigoCargo, self.Descripcion)


class EmpleadoCargo(models.Model):
    Empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    Cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    Desde = models.DateField(verbose_name="Fecha inicial del cargo")
    Hasta = models.DateField(verbose_name="Fecha final del cargo", null=True)

    def __str__(self):
        return "%s %s" % (self.Cargo.CodigoCargo, self.Empleado)


class TipoMovimiento(models.Model):
    Codigo = models.CharField(max_length=10)
    Descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.Codigo


class Movimiento(models.Model):
    Empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    FechaMovimiento = models.DateField(verbose_name="Fecha del movimiento")
    Concepto = models.CharField(max_length=200)


class DetalleMovimiento(models.Model):
    TipoMovimiento = models.ForeignKey(TipoMovimiento, on_delete=models.CASCADE, verbose_name="Tipo de movimiento")
    Monto = models.DecimalField(decimal_places=4, max_digits=10)
    AplicaDeduccion: bool = models.BooleanField(verbose_name="Aplicar deducción", default=False)

    def __str__(self):
        return "%s %s %s" % (self.TipoMovimiento, str(self.Monto), self.AplicaDeduccion)

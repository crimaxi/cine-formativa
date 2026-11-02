import uuid

from django.db import models


class Genero(models.Model):
    nombre = models.CharField("nombre", max_length=100, unique=True)

    class Meta:
        verbose_name = "género"
        verbose_name_plural = "géneros"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class Pelicula(models.Model):
    titulo = models.CharField("título", max_length=200)
    genero = models.ForeignKey(
        Genero,
        on_delete=models.CASCADE,
        related_name="peliculas",
        verbose_name="género",
    )
    sinopsis = models.TextField("sinopsis")
    duracion_minutos = models.PositiveSmallIntegerField("duración (minutos)")
    fecha_estreno = models.DateField("fecha de estreno")
    afiche = models.ImageField("afiche", upload_to="afiches/")
    precio = models.DecimalField("precio de entrada", max_digits=10, decimal_places=0)
    en_cartelera = models.BooleanField("en cartelera", default=True)

    class Meta:
        verbose_name = "película"
        verbose_name_plural = "películas"
        ordering = ["titulo"]

    def __str__(self):
        return self.titulo


class Ticket(models.Model):
    codigo = models.UUIDField(
        "código",
        default=uuid.uuid4,
        unique=True,
        editable=False,
    )
    pelicula = models.ForeignKey(
        Pelicula,
        on_delete=models.CASCADE,
        related_name="tickets",
        verbose_name="película",
    )
    nombre_comprador = models.CharField("nombre del comprador", max_length=150)
    correo_comprador = models.EmailField("correo del comprador")
    cantidad_entradas = models.PositiveSmallIntegerField("cantidad de entradas")
    fecha_compra = models.DateTimeField("fecha y hora de compra", auto_now_add=True)

    class Meta:
        verbose_name = "ticket"
        verbose_name_plural = "tickets"
        ordering = ["-fecha_compra"]

    def __str__(self):
        return f"Ticket {self.codigo} - {self.nombre_comprador}"

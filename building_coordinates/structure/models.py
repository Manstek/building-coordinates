from django.db import models
from core.models import CoordinateModel


class Structure(CoordinateModel):
    """Модель описывающая здание."""
    address = models.CharField(
        max_length=128,
        unique=True,
        verbose_name='адрес')

    class Meta:
        verbose_name = 'здание'
        verbose_name_plural = 'Здания'

    def __str__(self):
        return self.address


class Entrance(CoordinateModel):
    """Модель описывающая координаты входа в здание."""
    structure = models.ForeignKey(
        Structure,
        on_delete=models.SET_NULL,
        null=True)

    class Meta:
        verbose_name = 'вход'
        verbose_name_plural = 'Входы'

    def __str__(self):
        return f'{self.latitude}, {self.longitude}'

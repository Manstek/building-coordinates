from django.db import models


class CoordinateModel(models.Model):
    latitude = models.FloatField(verbose_name='широта')
    longitude = models.FloatField(verbose_name='долгота')

    class Meta:
        abstract = True

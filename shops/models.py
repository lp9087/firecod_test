from django.db import models
from datetime import datetime

from django.utils import timezone
from django.utils.timezone import localtime


class City(models.Model):
    """Города"""
    name = models.CharField('Город', max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class Street(models.Model):
    """Улицы"""
    name = models.CharField('Улица', max_length=150, default='null')
    city = models.ForeignKey(City, on_delete=models.PROTECT, )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Улица'
        verbose_name_plural = 'Улицы'


class Shops(models.Model):
    """Магазины"""
    name = models.CharField('Магазин', max_length=150, default='null')
    city = models.ForeignKey(City, on_delete=models.PROTECT, )
    street = models.ForeignKey(Street, on_delete=models.PROTECT)
    building = models.TextField('Дом')
    opening_time = models.TimeField('Время открытия', default=datetime.now(), blank=True, null=True)
    closing_time = models.TimeField('Время закрытия', default=datetime.now(), blank=True, null=True)

    @property
    def is_open(self):
        if self.opening_time < localtime().time() < self.closing_time:
            return 1
        else:
            return 0

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'

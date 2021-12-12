from django.db import models
from datetime import datetime


class City(models.Model):
    """Города"""
    name = models.CharField('Город', max_length=150)

    def __str__(self):
        return self.name


class Street(models.Model):
    """Улицы"""
    name = models.CharField('Улица', max_length=150, default='null')
    city = models.ForeignKey(City, on_delete=models.PROTECT, )

    def __str__(self):
        return self.name


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
        if self.opening_time < datetime.now().time() < self.closing_time:
            return True
        else:
            return False

    def __str__(self):
        return self.name

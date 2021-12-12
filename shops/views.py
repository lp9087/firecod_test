from django.shortcuts import render
from django.db import models
from rest_framework import generics, viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .models import City, Street
from .serializers import *


class CityViewSet(viewsets.ReadOnlyModelViewSet):
    """Вывод списка городов"""
    queryset = City.objects.all()
    serializer_class = CityListSerializer

    # def get_queryset(self):
    #   street = Street.objects.all()


class StreetViewSet(viewsets.ReadOnlyModelViewSet, ):
    """Вывод списка улиц"""

    serializer_class = StreetListSerializer
    filter_backends = (DjangoFilterBackend,)

    def get_queryset(self):
        queryset = Street.objects.filter(city_id=self.kwargs.get('city_id'))
        return queryset


class ShopCreateViewSet(viewsets.ModelViewSet):
    """Создание магазина"""
    serializer_class = ShopCreateSerializer

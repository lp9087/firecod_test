from django.db.models import Case, When, F
from django.shortcuts import render
from django.db import models
from django_property_filter import PropertyFilterSet, PropertyNumberFilter
from rest_framework import generics, viewsets
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, DateTimeFilter

from .models import City, Street, Shops
from .serializers import CityListSerializer, StreetListSerializer, ShopCreateSerializer, ShoplistSerializer


class CityViewSet(generics.ListAPIView):
    """Вывод списка городов"""
    queryset = City.objects.all()
    serializer_class = CityListSerializer


class StreetViewSet(generics.ListAPIView):
    """Вывод списка улиц"""

    serializer_class = StreetListSerializer
    filter_backends = (DjangoFilterBackend,)

    def get_queryset(self):
        queryset = Street.objects.filter(city_id=self.kwargs.get('city_id'))
        return queryset


class ShopViewSet(viewsets.ModelViewSet):
    """Для магазинов"""
    queryset = Shops.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['city', 'street',]

    def get_serializer_class(self):
        if self.action == 'create':
            return ShopCreateSerializer
        elif self.action == 'list':
            return ShoplistSerializer




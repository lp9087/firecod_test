from rest_framework import serializers

from .models import *


class CityListSerializer(serializers.ModelSerializer):
    """Вывод списка городов"""

    class Meta:
        model = City
        fields = ("name",)


class StreetListSerializer(serializers.ModelSerializer):
    """Вывод списка улиц"""

    class Meta:
        model = Street
        fields = ("name",)

class ShopCreateSerializer(serializers.ModelSerializer):
    """Создание магазина"""

    class Meta:
        model = Shops
        fields = "__all__"

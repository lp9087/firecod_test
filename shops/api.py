from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from .models import *
from .serializers import *


class cityViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = City.objects.all()
        serializer = CityListSerializer(queryset, many=True)
        return Response(serializer.data)

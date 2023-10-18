import json

from marshmallow import ValidationError
from django.views.generic import View

from rest_framework import generics
from techtest.regions.models import Region
from techtest.regions.schemas import RegionSchema
from techtest.utils import json_response


class RegionsListView(generics.ListCreateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSchema


class RegionView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSchema

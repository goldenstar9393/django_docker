from rest_framework import serializers
from techtest.regions.models import Region

class RegionSchema(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'code', 'name']

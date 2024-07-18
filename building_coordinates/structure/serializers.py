from rest_framework import serializers
from .models import Structure


class StructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Structure
        fields = ('id', 'address', 'latitude', 'longitude')

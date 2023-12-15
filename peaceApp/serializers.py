from rest_framework import serializers
from .models import Charities

class CharitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Charities
        fields = '__all__'

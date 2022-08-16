from rest_framework import serializers
from .models import ZoneMap


class ZoneMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZoneMap
        fields = ("num", "bcm", "pin", "gpio")

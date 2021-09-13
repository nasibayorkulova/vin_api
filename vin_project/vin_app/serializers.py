from rest_framework import serializers
from .models import VIN


class VINSerializer(serializers.Serializer):
    """
    VINSerializer
    Checks the transmitted Vin numbers for validation
    """
    vin = serializers.RegexField(
        "^[A-HJ-NPR-Za-hj-npr-z\d]{8}[\dX][A-HJ-NPR-Za-hj-npr-z\d]{2}\d{6}$",
        max_length=17,
        allow_blank=False,
    )


class VINReadSerializer(serializers.ModelSerializer):
    """
    VINReadSerializer ModelSerializer
    specifies the fields for response
    """
    class Meta:
        model = VIN
        fields = ('vin', 'year', 'make', 'model', 'type', 'color',
                  'dimensions', 'weight')

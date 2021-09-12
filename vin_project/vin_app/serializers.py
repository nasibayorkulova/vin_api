from rest_framework import serializers
from .models import VIN


# Create a VINSerializer to check the transmitted Vin numbers
# for validation.
class VINSerializer(serializers.Serializer):
    vin = serializers.RegexField(
        "^[A-HJ-NPR-Za-hj-npr-z\d]{8}[\dX][A-HJ-NPR-Za-hj-npr-z\d]{2}\d{6}$",
        max_length=17,
        allow_blank=False,
    )


# Create a VINReadSerializer and specify the fields for the JSON
# representation of the model in the response.
class VINReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = VIN
        fields = ('vin', 'year', 'make', 'model', 'type', 'color',
                  'dimensions', 'weight')

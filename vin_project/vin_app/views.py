import requests
from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import VIN
from .serializers import VINSerializer, VINReadSerializer


class VINViewset(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = VINSerializer
    queryset = VIN.objects.all()
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        vin_number = serializer.validated_data["vin"]
        try:
            # Checks that the vin number has already been stored
            # Sends the appropriate vehicle details
            vin = VIN.objects.get(vin=vin_number)
            response = Response(VINReadSerializer(vin).data)
            return response
        except VIN.DoesNotExist:
            # If vin number not saved,
            # the received data stores and sends
            url = 'https://8c5d8672-bbe7-4d14-8659-d85ea5237697.mock.pstmn.io/get'
            decode = requests.get(f'{url}')
            decode_vin = decode.json()
            year = decode_vin['decode']['vehicle'][0]['year']
            make = decode_vin['decode']['vehicle'][0]['make']
            model = decode_vin['decode']['vehicle'][0]['model']
            type = decode_vin['decode']['vehicle'][0]['engine']
            color = 'black'
            dimensions = '4330x1690x1505'
            weight = '1190'
            vin = VIN()
            vin.vin = vin_number
            vin.year = year
            vin.make = make
            vin.model = model
            vin.type = type
            vin.color = color
            vin.dimensions = dimensions
            vin.weight = weight
            vin.save()
            response = Response(VINReadSerializer(vin).data)
            return response

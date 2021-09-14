from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status

from .models import VIN
from .serializers import VINSerializer


# There initialize the APIClient app
client = Client()


class VINModelTest(TestCase):
    """ Test module for VIN model """

    def setUp(self):
        VIN.objects.create(
            vin='1P3EW65F4VV300949', year='2003', make='Plymouth',
            model='Prowler', type='Gas V10', color='green',
            dimensions='4730x1610x1600', weight='2200'
        )
        VIN.objects.create(
            vin='1REIT65F4VV300934', year='1999', make='Plymouth',
            model='Prowler', type='Gas M50', color='red',
            dimensions='6730x2610x2600', weight='3800'
        )

    def test_vin_year(self):
        vin1 = VIN.objects.get(vin='1P3EW65F4VV300949')
        vin2 = VIN.objects.get(vin='1REIT65F4VV300934')
        self.assertEqual(
            vin1.year, "2003")
        self.assertEqual(
            vin2.year, "1999")


class MySerializerTest(TestCase):
    """ Test module for VINSerializer model """

    def test_vin_validate(self):

        serializer = VINSerializer(data={'vin': '1P3EW65F4VV300949'})
        self.assertEqual(serializer.is_valid(), True)


class ViewTest(TestCase):
    """ Test module for GET all VIN API """

    def setUp(self) -> None:
        VIN.objects.create(
            vin='1P3EW65F4VV300949', year='2003', make='Plymouth',
            model='Prowler', type='Gas V10', color='green',
            dimensions='4730x1610x1600', weight='2200'
        )

    def test_response_status(self):
        # There getting API response
        response = client.post(reverse('vin_app:vin-list'), data={"vin": "1P3EW65F4VV300949"})
        # There checking response status
        self.assertEqual(response.status_code, status.HTTP_200_OK)

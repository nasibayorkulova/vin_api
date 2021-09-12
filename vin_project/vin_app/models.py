from django.db import models


# Create a model VIN to save vehicle details.
class VIN(models.Model):
    vin = models.CharField(max_length=17)
    year = models.CharField(max_length=4)
    make = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    color = models.CharField(max_length=15)
    dimensions = models.CharField(max_length=100)
    weight = models.CharField(max_length=10)

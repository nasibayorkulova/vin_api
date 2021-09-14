from django.db import models


class VIN(models.Model):
    """
    VIN Model
    There store vehicle details
    """
    vin = models.CharField(max_length=17)
    year = models.CharField(max_length=4)
    make = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    color = models.CharField(max_length=15)
    dimensions = models.CharField(max_length=100)
    weight = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.vin

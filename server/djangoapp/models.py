from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    country_of_origin = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dealer_id = models.IntegerField()

    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('HATCHBACK', 'Hatchback'),
        ('CONVERTIBLE', 'Convertible'),
        ('COUPE', 'Coupe'),
        ('TRUCK', 'Truck')
    ]
    type = models.CharField(max_length=25, choices=CAR_TYPES)

    year = models.IntegerField(validators=[
            MaxValueValidator(2023),
            MinValueValidator(2015)
        ])

    fuel_type = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.car_make.name + " " + self.name

# Uncomment the following imports before adding the Model code

from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Add any other fields you like here

    def __str__(self):
        return self.name


class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)  # Many-to-One relationship
    dealer_id = models.IntegerField()  # Refers to a dealer created in Cloudant database
    name = models.CharField(max_length=100)

    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        # Add more if needed
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')

    year = models.DateField()  # Changed from IntegerField to DateField as per your updated note

    def __str__(self):
        return f"{self.car_make.name} - {self.name}"  # Full name representation

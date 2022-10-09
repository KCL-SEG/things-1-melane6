from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models

class Thing(models.Model):
    """Thing model class"""

    name = models.CharField(max_length = 30, blank = False, unique = True)
    description = models.CharField(max_length = 120, unique = False, blank = True)
    quantity = models.IntegerField(
        validators = [
        MaxValueValidator(100,' Quantity must not be greater than 100'),
        MinValueValidator(0,'Quantity must not be negative')
        ]
        )

from django.core.validators import RegexValidator
from django.db import models

class Thing(models.Model):
    """Thing model class"""

    name = models.CharField(max_length = 30, blank = False, unique = True)
    description = models.CharField(max_length = 120, unique = False, blank = False)
    quantity = models.IntegerField(RegexValidator(
            regex = [0-100],
            message = 'Quantity must be a value from 0 to 100 (inclusive)'
    ))

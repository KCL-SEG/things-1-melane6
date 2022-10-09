from django.db import models

class Thing(models.Model):
    """Thing model class"""

    name = models.CharField(max_length = 30, blank = False)
    description = models.CharField(max_length = 100)
    quantity = models.IntegerField(blank = False)

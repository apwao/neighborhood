from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Neighborhood(models.Model):
    """
    class Neighborhood to facilitate creation of instances of a neighborhood
    """
    name=models.CharField(max_length=200)
    location=models.CharField(max_length=200)
    population=models.PositiveIntegerField()

    def create_neighborhood(self):
        """
        create_neighborhood method to help create a neighborhood
        and commit it to the database
        """
        
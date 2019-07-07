from django.db import models
from django.contrib.auth.models import User
from models import Neighborhood

# Create your models here.
class Neighborhood(models.Model):
    """
    class Neighborhood to facilitate creation of instances of a neighborhood
    """
    name=models.CharField(max_length=200)
    location=models.CharField(max_length=200)
    population=models.PositiveIntegerField()
    view_image=models.ImageField(upload_to='neighborhoods/')

    def create_neighborhood(self):
        """
        create_neighborhood method to help create a neighborhood
        and commit it to the database
        """
        self.save()
        
    def delete_neighborhood(self):
        """
        delete_neighborhood method to help remove an existing
        neighborhood from the database
        """
        self.delete()
        
    @classmethod    
    def find_neighborhood(cls,id):
        """
        find_neighborhood method to search through the neighborhood table in the
        database and return the specified neighborhood
        """
        hood=cls.objects.filter(id=id)
        return hood
        
    def __str__(self):
        return self.name
    
class Business(models.Model):
    """
    class Business to help a user register their business with the application
    """
    biz_name=models.CharField(max_length=300)
    owner=models.ForeignKey(User,default=1, on_delete=models.CASCADE)
    neighborhood_id=models.ForeignKey(Neighborhood, default=1, on_delete=models.CASCADE)
    email_address=models.EmailField(max_length=200)
    description=models.TextField()
    image=models.ImageField(upload_to='businesses/')
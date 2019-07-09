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
    
    def create_business(self):
        """
        create_business method to save an instance of a business
        to the database
        """
        self.save()
        
    def delete_business(self):
        """
        delete_business method to remove an existing business from
        the database
        """
        self.delete()
        
    @classmethod
    def search_business(cls,search_term):
        """
        method search_business to search the entire Business table
        in the database for the occurence of the search term
        """
        searched_business=cls.objects.filter(biz_name__icontains=businesses)
        return businesses
    
    @classmethod
    def search_by_neighborhood(cls,search_term):
        """
        method search_by_location to search entire business table for
        a business that matches the location input by a user
        """
        searched_location=Business.objects.filter(location__pk=location)
        return searched_location
    
class Profile(models.Model):
    """
    class Profile to facilitae saving od user's profile information to the database
    """
    name=models.CharField(max_length=200)
    user_id=models.ForeignKey(User,default=1)
    neighborhood=models.CharField(max_length=200)
    email_address=models.EmailField()
    profile_pic=models.ImageField(upload_to='profile_pics/')
    neighborhood_name=models.ForeignKey(Neighborhood, default=0)
    
    def create_profile(self):
        """
        create_profile method to save an instance of a profile
        to the database
        """
        self.save()
        
    def delete_profile(self):
        """
        delete_profile method to remove an existing profile from
        the database
        """
        self.delete()
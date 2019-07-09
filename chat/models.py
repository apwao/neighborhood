from django.db import models
from django.contrib.auth.models import User
from estate.models import Neighborhood


# Create your models here.
class Post(models.Model):
    """
    class Post to enable a user create and submit a post to be viewed by other users in a neighborhood
    """
    title=models.CharField(max_length=200)
    post=models.TextField()
    upload_date=models.DateTimeField(auto_now_add=True)
    posted_by=models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    neighborhood_id=models.ForeignKey(Neighborhood,on_delete=models.CASCADE)
    
    def save_post(self):
        """
        save post method to save post details provided 
        by the user to the database
        """
        self.save()
        
    def delete_post(self):
        """
        delete_post method to remove a post from the database
        """
        self.delete()

    
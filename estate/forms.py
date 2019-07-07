from models import Business
from django import forms


class BusinessForm(forms.ModelForm):
    """
    class BusinessForm to enable a user to register their businesses
    with the application
    """
    class Meta:
        model:Business
        exclude:['owner','neighborhood_id']
    
    
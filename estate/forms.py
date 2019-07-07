from models import Neighborhood
from django import forms

class NeighborhoodForm(forms.ModelForm):
    """
    class NeighborhoodForm to enable the Administrator to create
    instances of a neighborhood
    """
    class Meta:
        model:Neighborhood
        fields=('name','location','population')
    
    
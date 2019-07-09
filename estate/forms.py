from .models import Business,Profile
from django import forms

class BusinessForm(forms.ModelForm):
    """
    class BusinessForm to enable a user to register their businesses
    with the application
    """
    class Meta:
        model=Business
        fields=('biz_name','email_address','description','image')
       
class ProfileForm(forms.ModelForm):
    """
    class BusinessForm to enable a user to register their businesses
    with the application
    """
    class Meta:
        model=Profile
        fields=('name','email_address','neighborhood','neighborhood_name','profile_pic', )
        widget={
        'neighborhood_name':forms.SelectMultiple(),
        
            
        }
       
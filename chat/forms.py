from .models import Post
from django import forms

class PostForm(forms.ModelForm):
    """
    Class ProjectForm to enable a user to make an announcement in the neighborhood chatroom
    """
    class Meta:
        model=Post
        fields=('title','post')
        # widget={
        #     'neighborhood_name':forms.SelectMultiple(),
        # }
        
        
        
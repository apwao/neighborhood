from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect


# Create your views here.
def homepage(request):
    """
    homepage view function to display the landing page of the application
    """
    
    return render(request, 'homepage.html')
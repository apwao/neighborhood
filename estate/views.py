from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect


# Create your views here.
def homepage(request):
    """
    homepage view function to display the landing page of the application
    """
    neighborhoods=Neighborhood.objects.all()
    
    return render(request, 'homepage.html',{'neighborhoods',neighborhoods})

@login_required(login_url='/accounts/login/')
def view_businesses(request,neighborhood_id):
    """
    view_businesses function that displays registered businesses within a neighborhood
    """
    
    neighborhood_business=Business.objects.filter(neighborhood_id=neighborhood_id)
    
    return render(request, 'businesses.html',{'neighborhood_business':neighborhood_business})
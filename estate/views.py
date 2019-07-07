from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Neighborhood,Business,Profile
from .forms import BusinessForm,ProfileForm


# Create your views here.
def homepage(request):
    """
    homepage view function to display the landing page of the application
    """
    neighborhoods=Neighborhood.objects.all()
    
    return render(request, 'homepage.html',{'neighborhoods':neighborhoods})

@login_required(login_url='/accounts/login/')
def view_businesses(request,neighborhood_id):
    """
    view_businesses function that displays registered businesses within a neighborhood
    """
    
    neighborhood_business=Business.objects.filter(neighborhood_id=neighborhood_id)
    
    return render(request, 'businesses.html',{'neighborhood_business':neighborhood_business})

@login_required(login_url='/accounts/login/')
def business_form(request):
    """
    business_form view function to display a form to register a business
    """
    biz_form=BusinessForm()
    return render(request, 'business_form.html',{'biz_form':biz_form})

@login_required(login_url='/accounts/login/')
def process_biz_form(request):
    """
    process_biz_form function to process the post request of the business form
    """
    current_user=request.user 
    
    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            business_form=form.save(commit=True)
        else:
            raise Http404
        return redirect(view_businesses)
    else:
        biz_form=BusinessForm()
        
    return render(request, 'businesses.html')
@login_required(login_url='/accounts/login/')
def profile_form(request):
    """
    profile form view function to display a profile form to enable user to create
    a profile
    """
    current_user=request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            created_profile=form.save()
            return redirect(view_profile)
        else:
            return Http404
    else:
        form_profile=ProfileForm()
    return render(request, 'profile_form.html', {'form_profile':form_profile})

def view_profile(request):
    """
    view_profile view function to profile information provided by the user and store it the database
    """
    try:
        current_user=request.user 
        user_profile=Profile.objects.get(user_id=current_user.id)
    except:
        return redirect(profile_form)
    
    return render(request, 'profile.html',{'user_profile':user_profile})
    
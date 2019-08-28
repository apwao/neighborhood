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
def view_businesses(request):
    """
    view_businesses function that displays registered businesses within a neighborhood
    """
    
    neighborhood_business=Business.objects.all()
    print(neighborhood_business)
    
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
            business_form=form.save(commit=False)
            owner=current_user
            neighborhood_id=current_user.id
            form.save()
            
        else:
            raise Http404
        return redirect(homepage)
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
            created_profile=form.save(commit=False)
            created_profile.user_id = current_user
            # created_profile.neighborhood_name=
            created_profile.save()
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
        print(current_user.id)
        user_profile=Profile.objects.filter(user_id=current_user.id)
        print(user_profile)
        for i in user_profile:
            print(i.name)
        
    except:
        print('Error occured!')
        return redirect(profile_form)
    
    return render(request, 'profile.html',{'user_profile':user_profile,'current_user':current_user})
    
def search_results(request):
    
    if 'search_neighborhood' in request.GET and request.GET['search_neighborhood']:
        search_term=request.GET.get('search_neighborhood')
        
        searched_hood=Neighborhood.search_hoods(search_term)
        
    return render(request,'search.html',{'searched_hood':searched_hood})
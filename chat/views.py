from django.shortcuts import render,redirect
from .models import Post
from .forms import PostForm
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from estate.models import Neighborhood, Profile

# Create your views here.
def post_form(request):
    """
    post_form view function to display view form to the user
    """
    current_user = request.user
    print(current_user.username, current_user.id)
    profile_user = Profile.objects.get(user_id=current_user.id)
    locale_id = Neighborhood.objects.get(name=profile_user.neighborhood)
    if request.method=='POST':
        post_form=PostForm(request.POST)
        if post_form.is_valid():
        
            new_post=post_form.save(commit=False)
            new_post.posted_by=current_user
            new_post.neighborhood_id= profile_user.neighborhood_name
            new_post.neighborhood=profile_user.neighborhood
            new_post.save()
            post_form=PostForm()
            
    else:
       post_form=PostForm()
    user_profile = Profile.objects.get(user_id_id=current_user.id)
    # print(user_profile.user_id_id)
    posts=Post.objects.filter(neighborhood_id=user_profile.neighborhood_name_id)
    return render(request, 'post_form.html', {'post_form':post_form, "neighborhood_id":locale_id.id,'posts':posts})

# def view_posts(request):
#     """
#     view_posts view function to display the posts for a specific neighborhood
#     """
#     current_user=request.user
#     print('-'* 30)
#     user_profile = Profile.objects.get(user_id_id=current_user.id)
#     # print(user_profile.user_id_id)
#     posts=Post.objects.filter(neighborhood_id=user_profile.neighborhood_name_id)
#     return render(request, 'posts.html',{'posts':posts})
     


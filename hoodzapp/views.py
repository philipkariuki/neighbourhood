from django.shortcuts import render,redirect
from .models import Post, Thahood, UserProfile, Business
from .forms import NewPostForm, ProfileForm, UserForm
from django.http  import HttpResponse, Http404, HttpResponseRedirect
from registration.backends.simple.views import RegistrationView
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.db import transaction
from django.contrib import messages
from django.utils.translation import gettext as _

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):

	current_user = request.user	

	a_user = UserProfile.objects.filter(user_id=current_user.id).first()

    if custom_user is None:
        return redirect('profile_update')


	post = Post.objects.filter(neighbourhood_id=custom_user.neighbourhood.id)
	return render(request, 'index.html', {'post': post })




@login_required(login_url='/accounts/login/')
def post(request,id):
    try:
    	current_user = request.user
    	if request.method == 'POST':
    		params = request.POST
    		project_id = params.get(key="project_id", default=None)
    		comment = params.get(key="comment", default=None)

    		if comment is not None and project_id is not None:
    			project = Project.objects.get(id = id)
    			profile = UserProfile.objects.get(user=current_user)
    			cmt = Comments(comment_content=comment, project=project, profile= profile)
    			cmt.save_comment()
    	project = Project.objects.select_related().get(id = id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,"project2.html", {"project":project})





# @login_required(login_url='/accounts/login/')
# def project(request,project_id):
#     try:
#         project = Project.objects.get(id = project_id)
#     except ObjectDoesNotExist:
#         raise Http404()
#     return render(request,"project2.html", {"project":project})




def profile(request):
	try:
		argz = { 'user' : request.user }
	except ObjectDoesNotExist:
		raise Http404()
	return render(request,'profile.html', {'profile':argz} )


# def profile(request):
# 	try:
# 		profile =Profile.objects.get(id=request.user.id)
# 	except ObjectDoesNotExist:
# 		raise Http404()
# 	return render(request,'profile.html',{ 'profile':profile })




@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.userprofile)
    return render(request, 'profile_update.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })




@login_required(login_url='/accounts/login/')
def search_results(request):

    if 'projectsearch' in request.GET and request.GET["projectsearch"]:
        search_term = request.GET.get("projectsearch")
        searched_projects = Project.search_by_title(search_term)
        message = f"{search_term}"
        proj = Post.get_posts()

        return render(request, 'search.html',{"message":message,"projess": searched_projects, "prjz": proj})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})





@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.poster = current_user
            post.save()
        return redirect('index')
    else:
        form = NewPostForm()
    return render(request, 'newpost.html', {"form": form})




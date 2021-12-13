from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from awardsapp.forms import *
from django.contrib.auth.models import User
from awardsapp.models import *
from django import forms
from django.http.response import Http404, HttpResponseRedirect
import cloudinary
import cloudinary.uploader
import cloudinary.api

# Create your views here.

def index(request):
    images = Project.objects.all().order_by('-id')


    return render(request,'index.html', {'images':images})


@login_required(login_url="/accounts/login/")
def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()

    # project = Project.objects.filter(user_id=current_user.id).all()

    return render(request, "profile.html", {"profile": profile})


@login_required(login_url="/accounts/login/")
def create_profile(request):
    current_user = request.user
    title = "Create Profile"
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return HttpResponseRedirect('/')
    else:
        form = ProfileForm()
    return render(request, 'create_profile.html', {"form": form, "title": title})


@login_required(login_url="/accounts/login/")
def update_picture(request,id):
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user = user)
    form = UpdateProfileForm(instance=profile)
    if request.method == "POST":
            form = UpdateProfileForm(request.POST,request.FILES,instance=profile)
            if form.is_valid():
                profile = form.save(commit=False)
                profile.save()
                return redirect('profile')
    ctx = {"form":form}
    return render(request, 'update_profile.html', ctx)


@login_required(login_url="/accounts/login/")
def upload_project( request):
    if request.method =='POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
        return redirect('/')
    else:
        form =  ProjectForm()
    return render(request, 'project_form.html', {'form':form})

@login_required(login_url='/accounts/login/')
def search(request):
    if 'search' in request.GET and request.GET['search']:
        search_term = request.GET.get('search').lower()
        images = Project.search_project_name(search_term)
        message = f'{search_term}'
        return render(request, 'search.html', {'found': message, 'images': images})
    else:
        message = 'Not found'
        return render(request, 'search.html', {'danger': message})


def project_details(request, project_id):
    project = Project.objects.get(id=project_id)
    return render(request, "project.html", {"project": project })

@login_required(login_url="/accounts/login/")
def rating(request,id):
    if request.method == 'POST':
        project = Project.objects.get(id = id)
        current_user = request.user
        design = request.POST['design']
        content = request.POST['content']
        usability = request.POST['content']
        Rating.objects.create(
            project=project,
            user=current_user,
            design=design,
            usability=usability,
            content=content,
            average=round((float(design)+float(usability)+float(content))/3,2),)
        return render(request, 'project.html',{'project':project})
    else:
        project = Project.objects.get(id = id)
        return render(request, 'project.html',{'project':project})
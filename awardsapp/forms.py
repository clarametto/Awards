from django import forms
from django.db.models import fields
from django.forms import ModelForm
from .models import *


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','email']

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture','bio','contact']

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['photo', 'title', 'description', 'category', 'location', 'project_url']


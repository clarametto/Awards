from awardsapp import *
import cloudinary
import cloudinary.uploader
import cloudinary.api
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request,'index.html')
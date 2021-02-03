from django.shortcuts import render,redirect,get_object_or_404
from math import ceil
import json

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
from django.http import HttpResponse
from django.db import models
from django.contrib import messages

def index(request):
    return render(request,"home.html")
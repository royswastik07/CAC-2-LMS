from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Usertbl,Orderstbl
import uuid

# Create your views here.
def index(request):
    return render(request,"userM/home.html")
def signup_login(request):
    return render(request,"userM/signup-login.html")
def loginerror(request):
    return render(request,"userM/loginerror.html")
def userwelcome(request):
    return render(request,"userM/userwellcome.html")
def requestorder(request):
    return render(request,"userM/request.html")
def requestdone(request):
    return render(request,"userM/requestdone.html")
def trackstatus(request):
    return render(request,"userM/trackstatus.html")
def showstatus(request):
    return render(request,"userM/showstatus.html")
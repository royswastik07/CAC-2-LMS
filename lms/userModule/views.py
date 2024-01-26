from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"userM/home.html")
def login(request):
    return render(request,"userM/login.html")
def signup(request):
    return render(request,"userM/signup.html")
def userwelcome(request):
    return render(request,"userM/userwellcome.html")
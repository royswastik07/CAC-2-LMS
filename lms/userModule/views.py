from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"userM/home.html")
def login_signup(request):
    return render(request,"userM/login-signup.html")
def userwelcome(request):
    return render(request,"userM/userwellcome.html")
def requestorder(request):
    return render(request,"userM/request.html")
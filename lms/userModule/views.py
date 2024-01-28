from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"userM/home.html")
def login_signup(request):
    return render(request,"userM/login-signup.html")
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
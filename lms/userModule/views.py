from django.shortcuts import render,redirect

# Create your views here.
def studentlogin(request):
    return render(request,"userM/studentlogin.html")
def teacherlogin(request):
    return render(request,"userM/teacherlogin.html")
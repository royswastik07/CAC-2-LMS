from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Usertbl
import uuid

# Create your views here.
def index(request):
    return render(request,"userM/home.html")
def signup_login(request):
    return render(request,"userM/signup-login.html")

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        usertype = request.POST['usertype']
            
        if not User.objects.filter(username=username).exists():
            if pass1==pass2:
                
                
                myuser = User.objects.create_user(username, email, pass1)
                if usertype == "staff":
                    myuser.is_staff=True
                myuser.save()
                
                user_tbl = Usertbl(
                    user = myuser,
                    usertype = usertype,
                    username = username,
                    useremail = email,
                    
                    
                )
                user_tbl.save()
                return render(request,"userM/signup-login.html",{'success_message': "User got Created"})
            else:
                return render(request,"userM/signup-login.html",{'password_error_message': "Check your conformation password"})
        else:
            return render(request,"userM/signup-login.html",{'username_error_message': "Username Already Exist"})
          
    return render(request, "userM/signup-login.html")

# def signup(request):
#     if request.method == 'POST':
#         Userregnoid = request.POST.get('regnoid')
#         Username = request.POST.get('name')
#         Password = request.POST.get('password')
#         Useremail = request.POST.get('email')
#         Usertype = request.POST.get('userType')

#         # Check if a user with the given email already exists
#         if User.objects.filter(email=Useremail).exists():
#             messages.error(request, "User with this email already exists.")
#             return redirect('signup')

#         is_staff = (Usertype == 'staff')

#         # Create a new user using Django's User model
#         my_user = User.objects.create_user(username=Username, email=Useremail, password=Password)

#         # Save the user profile information in your custom model
#         user_profile = Usertbl(
#             username=Username,
#             useremail=Useremail,
#             userRegnoID=Userregnoid,
#             is_staff=is_staff
#         )
#         user_profile.save()

#         print("User profile insertion started")
#         print(f"Is_staff: {is_staff}")

#         return redirect('login')
#     else:
#         return render(request, "userM/signup-login.html")  # Signup 
# def login(request):
#     if request.method == 'POST':
#         Useremail = request.POST.get('email')
#         Password = request.POST.get('password')
#         Usertype = request.POST.get('userType')

#         user = authenticate(request, useremail = Useremail, password = Password )

#         if user is not None:
#             user_profile = user.userprofile

#             if Usertype == 'user' and not user_profile.is_staff:
#                 login(request, user)
#                 return redirect('index')
#             elif Usertype == 'host' and user_profile.is_staff:
#                 login(request, user)
#                 return redirect('host')
#             else:
#                 messages.error(request, f"No {Usertype.capitalize()} account found with this email.")
#         else:
#             messages.error(request, "Invalid email or password.")

#     return render(request,"userM/signup-login.html") 
    



def user_login(request):
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['password']
        user_type = request.POST['userType']

        # Perform authentication
        user = authenticate(username=username, password=password)

        if user is not None:
            # Log the user in
            login(request, user)
            if not user.is_staff:
                # messages.success(request, 'Login successful.')
                return redirect('user-w')  # Redirect to your home page or any desired URL after login
            elif user.is_staff:
                return redirect('track-sts')
        else:
            # messages.error(request, 'Invalid login credentials.')
            return render(request,'userM/loginerror.html')  # Redirect back to the login page in case of authentication failure
    else:
        return render(request, "userM/signup-login.html")

def loginerror(request):
    return render(request,"userM/loginerror.html")
@login_required (login_url='login')
def userwelcome(request):
    return render(request,"userM/userwellcome.html")
@login_required (login_url='login')
def requestorder(request):
    return render(request,"userM/request.html")
@login_required (login_url='login')
def payment(request):
    return render(request,"userM/payment.html")
@login_required (login_url='login')
def requestdone(request):
    return render(request,"userM/requestdone.html")
@login_required (login_url='login')
def trackstatus(request):
    return render(request,"userM/trackstatus.html")
@login_required (login_url='login')
def showstatus(request):
    return render(request,"userM/showstatus.html")
@login_required (login_url='login')
def complaints(request):
    return render(request,"userM/complaint.html")
@login_required (login_url='login')
def signout(request):
    logout(request)
    return redirect('home')
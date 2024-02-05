from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Usertbl, Orderstbl, Payment, Complaint
from django.http import HttpResponse

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


@login_required(login_url='login')
def requestorder(request):
    if request.method == 'POST':
        # Extract form data from the request
        name = request.POST.get('Name')
        reg_no = request.POST.get('RegNo')
        department = request.POST.get('Department')
        service_type = request.POST.get('Service')
        quantity = request.POST.get('Quantity')
        amount = request.POST.get('Amount')
        expected_delivery_date = request.POST.get('Delivery')

        # Perform basic form validation (you can add more checks)
        if not name or not reg_no or not department or not service_type or not quantity or not amount or not expected_delivery_date:
            return HttpResponse("All fields are required.")

        # Convert lazy-loaded user to Usertbl instance
        user_instance = User.objects.get(username=request.user.username).usertbl

        # Create an Orderstbl instance and save it to the database
        order = Orderstbl(
            user=user_instance,
            service_type=service_type,
            quantity=quantity,
            amount=amount,
            expected_delivery_date=expected_delivery_date,
            payment_completed=False
        )
        order.save()

        # Redirect to a success page or home page
        return redirect('payment', order_id=order.id) # Replace 'home' with the actual URL name of your home page

    
    return render(request,"userM/request.html")
@login_required(login_url='login')
def payment(request, order_id):
    # Retrieve the order from the database
    order = get_object_or_404(Orderstbl, id=order_id)

    if request.method == 'POST':
        # Process the payment (replace with your payment processing logic)

        # Assuming payment is successful, update the order's payment status to True
        order.payment_completed = True
        order.save()

        # Get the payment amount from the form data
        payment_amount_str = request.POST.get('amount', '0')  # Default to '0' if 'amount' is not present
        try:
            payment_amount = int(payment_amount_str)
        except ValueError:
            # Handle the case where 'amount' is not a valid integer
            payment_amount = 0

        # Create a Payment instance
        payment = Payment(order=order, amount_paid=payment_amount, payment_status='SUCCESS')
        payment.save()

        # Pass user name and order ID to the template context
        context = {
            'order': order,
            'user_name': order.user.username,
            'tracking_id': order.id,
        }

        # Redirect to a success page or home page
        return render(request, 'userM/requestdone.html', context)  # Use your template name

    return render(request, "userM/payment.html", {'order': order})
@login_required (login_url='login')
def requestdone(request):
    return render(request,"userM/requestdone.html")
@login_required (login_url='login')
def trackstatus(request):
    if request.method == 'POST':
        tracking_id = request.POST.get('TrackingId')

        # Query the database to get the order with the provided Tracking ID
        order = get_object_or_404(Orderstbl, id=tracking_id)

        # Pass the order information to the template context
        context = {
            'order': order,
            # 'status': order.status  # Replace 'status' with the actual field name in your Orderstbl model
        }

        return render(request, 'userM/showstatus.html', context)

    return render(request, 'userM/trackstatus.html')
@login_required (login_url='login')
def showstatus(request):
    return render(request,"userM/showstatus.html")
@login_required(login_url='login')
def complaints(request):
    if request.method == 'POST':
        # Assuming the user is logged in, retrieve the user instance from the request
        user_instance = Usertbl.objects.get(user=request.user)

        user_name = request.POST.get('user_name')
        complaint_text = request.POST.get('complaint_text')

        # Perform basic form validation (you can add more checks)
        if not user_instance or not user_name or not complaint_text:
            return render(request, 'userM/complaint.html', {'error_message': 'All fields are required.'})

        # Create a Complaint instance without the 'user' field
        complaint = Complaint.objects.create(user_name=user_name, complaint_text=complaint_text)

        # Optionally, you can add a success message or just return to the complaint page.
        return render(request, 'userM/complaint.html', {'success_message': 'Complaint submitted successfully.'})

    return render(request, 'userM/complaint.html')
@login_required (login_url='login')
def signout(request):
    logout(request)
    return redirect('home')
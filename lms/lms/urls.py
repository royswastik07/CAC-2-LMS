"""
URL configuration for lms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from userModule.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",index,name="home"),
    path("signup-login",signup_login,name="signup-login"),
    path('signup',signup,name='signup'),
    path('user_login',user_login,name='user_login'),
    path("loginerror",loginerror,name="login-error"),
    path("userwellcome",userwelcome,name="user-w"),
    path("requestorders",requestorder,name="order-req"),
     path('payment/<int:order_id>/', payment, name='payment'),
    path("requestdone",requestdone,name="order-reqdone"),
    path("trackstatus",trackstatus,name="track-sts"),
    path('showstatus/<int:order_id>/', showstatus, name='showstatus'),
    path('complaints/', complaints, name='complaints'),
    path("signout",signout,name="logout")
]

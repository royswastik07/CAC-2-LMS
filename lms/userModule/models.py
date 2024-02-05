from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime
import uuid
from django.contrib.auth.models import User


# Create your models here.
class Usertbl(models.Model):
    USER_TYPE_CHOICES = [
        ('USER', 'user'),
        ('STAFF', 'staff'),
    ]
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    usertype = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    username = models.TextField(max_length=255,blank=False)
    useremail = models.EmailField(max_length=254,unique=True,blank=False,null=False)
    is_staff = models.BooleanField(default=False) #New Field For Host







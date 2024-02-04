from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime
import uuid


# Create your models here.
class Usertbl(models.Model):
    USER_TYPE_CHOICES = [
        ('USER', 'user'),
        ('STAFF', 'staff'),
    ]
    userRegnoID = models.IntegerField(primary_key=True)
    usertype = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    username = models.TextField(max_length=255,blank=False)
    useremail = models.EmailField(max_length=254,unique=True,blank=False,null=False)
    is_staff = models.BooleanField(default=False) #New Field For Host
 
    def __str__(self):
        return f"{self.username} ({self.userRegnoID})"







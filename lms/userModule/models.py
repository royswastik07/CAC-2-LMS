from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime
import uuid

# Create your models here.
class Usertbl(models.Model):
    userRegnoID = models.IntegerField(primary_key=True)
    username = models.TextField(max_length=255,blank=False)
    useremail = models.EmailField(max_length=254,unique=True,blank=False,null=False)
    def __str__(self):
        return f"{self.username} ({self.userRegnoID})"

class Orderstbl(models.Model):
    ORDER_DEPT_CHOICES = [
        ('dept1', 'Department 1'),
        ('dept2', 'Department 2'),
    ]

    ORDER_SERVICE_CHOICES = [
        ('service1', 'Service 1'),
        ('service2', 'Service 2'),
    ]

    orderid = models.AutoField(primary_key=True)
    userRegnoID = models.ForeignKey(Usertbl, on_delete=models.CASCADE)  # ForeignKey for the one-to-many relationship
    dept = models.CharField(max_length=10, choices=ORDER_DEPT_CHOICES)
    service = models.CharField(max_length=10, choices=ORDER_SERVICE_CHOICES)
    quantity = models.IntegerField(validators=[MinValueValidator(5), MaxValueValidator(30)])
    orderdate = models.DateField(auto_now_add=True)
    expected_delivery = models.DateField()

    def __str__(self):
        return f"Order {self.orderid} - User {self.userRegnoID.username}"






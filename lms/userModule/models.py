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
        ('ADMIN', 'admin'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    usertype = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    username = models.TextField(max_length=255, blank=False)
    useremail = models.EmailField(max_length=254, unique=True, blank=False, null=False)
    is_staff = models.BooleanField(default=False)  # New Field For Host
    is_admin = models.BooleanField(default=False)  # New Field For Admin

    def __str__(self):
        return self.username

class Orderstbl(models.Model):
    SERVICE_TYPE_CHOICES = [
        ('Dryclean', 'Dryclean'),
        ('NormalWash', 'NormalWash'),
    ]

    user = models.ForeignKey(Usertbl, on_delete=models.CASCADE,null=False)
    service_type = models.CharField(max_length=20, choices=SERVICE_TYPE_CHOICES,null=False)
    quantity = models.IntegerField()
    amount = models.IntegerField() 
    expected_delivery_date = models.DateField()
    payment_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}'s Order ({self.service_type} - {self.quantity} items)"


class Payment(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('SUCCESS', 'Success'),
        ('PENDING', 'Pending'),
        ('FAILED', 'Failed'),
    ]

    order = models.ForeignKey(Orderstbl, on_delete=models.CASCADE, null=False)
    amount_paid = models.IntegerField()
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES, default='PENDING')
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.order.user.username}'s Payment ({self.amount_paid} - {self.payment_status})"

class Complaint(models.Model):
    user_name = models.CharField(max_length=50, blank=False)
    complaint_text = models.TextField(max_length=50, blank=False)

    def __str__(self):
        return f"Complaint by {self.user_name} for user {self.user.username}"

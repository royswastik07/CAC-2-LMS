# userModule/admin.py

from django.contrib import admin
from .models import Usertbl,Orderstbl,Payment,Complaint

admin.site.register(Usertbl)
admin.site.register(Orderstbl)
admin.site.register(Payment)
admin.site.register(Complaint)

# userModule/admin.py

from django.contrib import admin
from .models import Usertbl

class userAdmin(admin.ModelAdmin):
    list_display = ('display_info', 'usertype', 'username', 'useremail', 'is_staff')

    def display_info(self, obj):
        return f'{obj.id} - {obj.username}'

admin.site.register(Usertbl, userAdmin)

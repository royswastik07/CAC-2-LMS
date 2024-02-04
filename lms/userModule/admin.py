from django.contrib import admin
from userModule.models import Usertbl

# Register your models here.
class userAdmin(admin.ModelAdmin):
    list_display=('userRegnoID','usertype','username','useremail')
admin.site.register(Usertbl,userAdmin)
# admin.site.register(Usertbl,userAdmin)
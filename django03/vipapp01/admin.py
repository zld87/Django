from django.contrib import admin
from .models import *



class User_Admin(admin.ModelAdmin):
    list_display = ['user','pwd','create_time','update_time','userphone']







admin.site.register(Top_Register_User,User_Admin)
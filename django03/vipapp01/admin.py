from django.contrib import admin
from .models import *



class User_Admin(admin.ModelAdmin):
    list_display = ['user','pwd','create_time','update_time','userphone','update_image']
    list_filter = ['user']
    search_fields = ['user']
    list_per_page = 10








admin.site.register(Top_Register_User,User_Admin)

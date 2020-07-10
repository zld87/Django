from django.contrib import admin
from django.urls import path,include
from vipapp01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.register,name='register'),
    path('registerdetail/',views.registerdetail,name='registerdetail'),
    path('login/',views.login,name='login'),
    path('login_show/',views.login_show,name='login_show'),
    path('login_handle/',views.login_handle,name='login_handle'),
    path('loginextend/',views.loginextend,name='loginextend'),
    path('loginout/',views.loginout,name='loginout'),
    path('middleware/',views.exception),
    path('verifycode/',views.verifycode)
]

app_name='vipapp01'
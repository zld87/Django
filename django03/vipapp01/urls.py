from django.contrib import admin
from django.urls import path,include,re_path
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
    path('verifycode/',views.verifycode),
    path('uploadfile/',views.uploadfile),
    path('uploadhaldle/',views.uploadhaldle),
    re_path('search_user/(?P<page>\d+)/(?P<num>\d+)/',views.search_user,name='search_user'),
    path('process_template_response/',views.process_template_response),
    path('ld_home/',views.my_home,name='ld_home'),
    path('ld_home2/',views.my_home2,name='ld_home2'),
    path('ld_home3/',views.my_home3,name='ld_home3'),

]

app_name='vipapp01'
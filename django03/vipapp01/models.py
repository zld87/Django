#coding=utf-8
from django.db import models
from django.db.models import F,Q,Max,Min,Avg,Count



#自定义管理器
class User_Manager(models.Manager):
    def get_queryset(self):
        return super(User_Manager,self).get_queryset()
    def create(self,adduser,addpwd,phone=None):
        topuser = Top_Register_User()
        topuser.user=adduser
        topuser.pwd=addpwd
        topuser.userphone=phone
        return topuser

class Group_Manager(models.Manager):
    def create(self,groupname,describe):
        topgroup=Top_User_Group()
        topgroup.group_name=groupname
        topgroup.describe=describe
        return topgroup


#
class Top_User_Group(models.Model):
    group_name=models.CharField(max_length=200,db_column='groupname')
    describe=models.CharField(max_length=10000,null=True)
    group_state=models.BooleanField(db_column='state',default=False)
    group_create=models.DateTimeField(auto_now_add=True,db_column='create_time')
    group_update=models.DateTimeField(auto_now=True,db_column='update_time')
    isdelete=models.BooleanField(default=False)
    groupmanager=Group_Manager()
    #group_user=models.ManyToManyField('Top_Register_User') #如果模型类未在此之前定义则使用引号
    class Meta:
        db_table='top_user_group'
    def __str__(self):
        return self.group_name


class Top_Register_User(models.Model):
    user=models.CharField(max_length=200,db_column='username',blank=False,null=False)
    pwd=models.CharField(max_length=200,db_column='password')
    create_time=models.DateTimeField(auto_now_add=True)
    update_time=models.DateTimeField(auto_now=True)
    isdelete=models.BooleanField(default=False)
    userManager=User_Manager()
    userphone=models.CharField(max_length=100,null=True,blank=True,db_column='phone')
    update_image=models.ImageField(upload_to='vipapp01',null=True,blank=True)
    user_group=models.ManyToManyField(Top_User_Group)
    class Meta:
        db_table='top_register_user'
    def __str__(self):
        return self.user


class Top_Role(models.Model):
    role_name=models.CharField(max_length=100)
    role_user=models.ManyToManyField(Top_Register_User)






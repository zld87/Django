#coding=utf-8
from django.db import models
from django.db.models import F,Q,Max,Min,Avg,Count



#自定义管理器
class User_Manager(models.Manager):
    def get_queryset(self):
        return super(User_Manager,self).get_queryset().filter(pwd='63648215zld')
    def create(self,adduser,addpwd,phone=None):
        topuser = Top_Register_User()
        topuser.user=adduser
        topuser.pwd=addpwd
        topuser.userphone=phone
        return topuser

class Group_Manager(models.Manager):
    def create(self,groupname):
        topgroup=Top_User_Group()
        topgroup.group_name=groupname
        return topgroup



class Top_User_Group(models.Model):
    group_name=models.CharField(max_length=200,db_column='groupname')
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
    user_group=models.ManyToManyField(Top_User_Group)
    class Meta:
        db_table='top_register_user'
    def __str__(self):
        return self.user


class Top_Role(models.Model):
    role_name=models.CharField(max_length=100)
    role_user=models.ManyToManyField(Top_Register_User)
    class Meta:
        db_table='top_role'
    def __str__(self):
        return self.role_name



class Project(models.Model):
    project_name=models.CharField(max_length=200)                                       #项目名称
    create_time=models.DateTimeField(auto_now_add=True)
    update_time=models.DateTimeField(auto_now=True)
    describe=models.CharField(max_length=2000)                                          #备注，描述
    class Meta:
        db_table='Project'
    def __str__(self):
        return self.project_name

class Modular(models.Model):
    modular_name=models.CharField(max_length=50)
    create_time=models.DateTimeField(auto_now_add=True)
    update_time=models.DateTimeField(auto_now=True)
    modular_project=models.ForeignKey(Project,on_delete=models.PROTECT)
    modular_Sub =models.ForeignKey('self',null=True,blank=True,on_delete=models.PROTECT)
    class Meta:
        db_table='Modular'
    def __str__(self):
        return self.modular_name


class Test_Plan(models.Model):
    plan_name = models.CharField(max_length=2000)                                       #计划名称
    plan_state = models.IntegerField(default=1)                                         #当前状态1.未开始 2.进行中 3.已完成 4.错误
    phase =models.IntegerField(default=4)                                               #测试阶段1.冒烟测试 2.系统测试 3.回归测试，4.未开始
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    plan_Maintainer = models.ForeignKey(Top_Register_User,on_delete=models.PROTECT)     #负责人
    plan_project = models.ForeignKey(Project,on_delete=models.PROTECT)                  #项目名称
    plan_case = models.ManyToManyField('Test_Case')                                     #测试计划关联用例
    class Meta:
        db_table='Test_Plan'
    def __str__(self):
        return self.plan_name

class Test_Case(models.Model):
    case_name=models.CharField(max_length=2000)                                         #用例名称
    test_mode = models.IntegerField(default=1)                                          #测试方式 1.手动 2.自动
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    case_type = models.IntegerField(default=1)                                          #用例类型  1.功能 2.接口 3.性能
    case_priority = models.IntegerField(default=1)                                      #用例优先级 1.P1  2.P2  3.P3  4.P4
    case_project =models.ForeignKey(Project,on_delete=models.PROTECT)                   #项目名称
    case_modular = models.ForeignKey(Modular,on_delete=models.PROTECT)                  #模块名称
    case_Maintainer=models.ForeignKey(Top_User_Group,on_delete=models.PROTECT)          #维护人
    case_result = models.IntegerField(default=3)                                        #1.通过  2.失败  3.未执行 4.阻塞
    case_plan = models.ManyToManyField(Test_Plan)                                       #用例关联测试计划
    class Meta:
        db_table='Test_Case'
    def __str__(self):
        return self.case_name

class function_Case_Content(models.Model):
    content_parameter=models.TextField(max_length=50000)                                #用例内容：[{步骤:结果},{步骤,结果}....]
    describe= models.TextField(max_length=2000)                                         #备注描述
    function_Preconditions =models.TextField(max_length=2000)                           #前置条件
    class Meta:
        db_table='function_Case_Content'


class PeInt_Case_Content(models.Model):
    function_Preconditions =models.TextField(max_length=2000)                            #前置条件
    content_parameter=models.ManyToManyField('Interface_Case')                           #关联接口
    class Meta:
        db_table='PeInt_Case_Content'



class Interface_Case(models.Model):
    headers = models.CharField(max_length=4000,null=True,blank=True)                     #请求头
    server = models.CharField(max_length=2000)                                           #域名或ip
    port = models.CharField(max_length=100,null=True,blank=True)                         #端口
    path = models.TextField(max_length=50000)                                            #路径
    parameter = models.TextField(max_length=50000,null=True,blank=True)                  #参数
    method = models.CharField(max_length=100)                                            #请求方式
    protocol= models.CharField(max_length=100)                                           #协议
    Assertion=models.TextField(max_length=50000,null=True,blank=True)                    #断言
    state = models.IntegerField(default=3)                                               #1.通过 2.未通过 3.未执行
    content_parameter=models.ManyToManyField('PeInt_Case_Content')                       #关联接口用例
    class Meta:
        db_table='Interface_Case'































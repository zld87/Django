from django.shortcuts import render,redirect
from .models import *
from django.http import *
from django.urls import reverse
from django.db.models import F,Q
from datetime import timedelta,datetime
import json,os
from .task import *
from PIL import Image, ImageDraw, ImageFont
from django.conf import settings
from django.core.paginator import *
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from deepdiff import DeepDiff

#注册
def register(req):
    #return redirect(reverse('vipapp01:login_show'))
    return render(req, 'vipapp01/register.html')

#登陆
def login(req):
    return render(req,'vipapp01/login.html')

#注册处理
@cache_page(60)
def registerdetail(req):
    if req.method=='POST':
        username=req.POST['username']
        pwd=req.POST['pwd']
        phone=req.POST.get('phone',default=None)
        if username == '':
            return redirect(reverse("vipapp01:register"))
        elif not Top_Register_User.userManager.filter(user__exact=username):
            new_user=Top_Register_User.userManager.create(username,pwd,phone)
            new_user.save()
            data={"code": 200,"msg":'注册成功,请立即登陆',"data":reverse('vipapp01:login')}
            return HttpResponse(json.dumps(data))
                #redirect(reverse('vipapp01:login'))
        else:
            data={"code": 200,"msg": '账号已被注册，请重新注册',"data":reverse('vipapp01:register')}
            return HttpResponse(json.dumps(data))
                #redirect(reverse('vipapp01:register'))

#登陆处理
def login_handle(req):
    if req.method=='POST':
        username=req.POST['username']
        pwd=req.POST['pwd']
        if Top_Register_User.userManager.get(user=username):
            user=Top_Register_User.userManager.get(user=username)
            if user.pwd==pwd:
                req.session['myuser']=username
                req.session['pwd']=pwd
                req.session.set_expiry(0)
                req.session.flush()
                #req.session.clear()
                data = {"code": 200, "msg": '返回成功', "data": reverse('vipapp01:search_user',kwargs={'num':10,'page':1})}
                #return HttpResponse(json.dumps(data))
                #return redirect(reverse('vipapp01:login_show'))
            else:
                data = {"code": 200, "msg": '返回成功', "data": reverse('vipapp01:login')}
                #return HttpResponse(json.dumps(data))
                return redirect(reverse("vipapp01:login"))
        else:
            print('11111')
            data = {"code": 200, "msg": '返回成功', "data": reverse('vipapp01:login')}
            return HttpResponse(json.dumps(data))
                #redirect(reverse('vipapp01:register'))


def login_show(req):
    myuser=req.session['myuser']
    pwd=req.session['pwd']
    content={'myuser':myuser,'pwd':pwd}
    #req.session.clear()
    return render(req,'vipapp01/login_show.html',content)

#转义
def loginextend(req):
    content={'f1':'<h1>abcd</h1>'}
    return render(req,'vipapp01/loginextend.html',content)

def loginout(req):
    response=HttpResponse()
    response.delete_cookie("csrftoken")
    return response

#验证码
def verifycode(req):
    import random
    from io import BytesIO
    buf=BytesIO()
    width=100
    height=25
    bgColor=(random.randrange(50,100),random.randrange(50,100),0)
    image=Image.new('RGB',(width,height),bgColor)
    draw=ImageDraw.Draw(image)
    font=ImageFont.truetype('/System/Library/Fonts/SFNSItalic.ttf',20)
    test='zldtestverifycode'
    newverifycode=''
    for i in range(0,4):
        newverifycode1=test[random.randrange(0,len(test))]
        newverifycode +=newverifycode1
        draw.text((i*25,0),
                  newverifycode1,
                  (255,255,255),
                  font=font)
    req.session['newverifycode']=newverifycode
    image.save(buf,format='png')
    return HttpResponse(buf.getvalue(),content_type='image/png')

#中间件
def exception(req):
    #a=int('abc')
    #return HttpResponse('安全')
    return render(req, 'vipapp01/register.html')


#文件上传
def uploadfile(req):
    return render(req, 'vipapp01/uploadfile.html')

#文件处理
def uploadhaldle(req):
    if req.method=='POST':
        pic=req.FILES.get('pic1')
        #content=req.FILES.get('content')
        print(123)
        picpath=os.path.join(settings.MEDIA_ROOT,pic.name)
        with open(picpath,'wb') as f:
            for i in pic.chunks():
                f.write(i)
        return HttpResponse(picpath)
    else:
        return HttpResponse('error')

#重写json处理datetime对象时间
class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self,obj)

#调用process_template_response中间件
class Foo():
    def __init__(self,requ):
        self.req=requ
    def render(self):
        return HttpResponse(self.req.path_info)

def process_template_response(req):
    print("执行index")
    obj=Foo(req)
    return obj


#用户列表页增删改查
def search_user(req,page=1,num=10):
    if req.method== 'GET':
        all_user_num=Top_Register_User.userManager.count()
        all_user_list=Top_Register_User.userManager.all()
        onepage_list=Paginator(all_user_list,num)
        page=onepage_list.page(page)
        print(page,'zzzzzz')
        userlist=[]
        for i in page:
            pk=i.pk
            user=i.user
            create_time=i.create_time.strftime('%Y-%m-%d %H:%M:%S')
            update_time=i.update_time.strftime('%Y-%m-%d %H:%M:%S')
            userphone=i.userphone
            #user_group=i.user_group
            user_info={'pk':pk,'user':user,'create_time':create_time,'update_time':update_time,'userphone':userphone}
            userlist.append(user_info)
        data = {"code": 200, "msg": '返回成功','num': len(page.object_list),'data': userlist}
        #print(userlist)
        return HttpResponse(json.dumps(data,ensure_ascii= False), content_type= 'application/json')
        #json_dumps_params返回中文unicode
        #return JsonResponse(data,json_dumps_params={'ensure_ascii':False})
    elif req.method == 'POST':
        usernameinfo = req.POST.getlist('username',default='未登录')
        status = req.POST['status']
        if usernameinfo == '未登录':
            data = {"code":200,'msg':'没有该账号'}
            return HttpResponse(json.dumps(data, ensure_ascii=False), content_type='application/json')
        #删除用户
        elif status== 2:
            usernameinfo= req.POST.getlist('username')
            for username in usernameinfo:
                selectuser = Top_Register_User.userManager.get(user=username)
                selectuser.delete()
                data = {'code':200,'msg':'删除成功'}
            return HttpResponse(json.dumps(data, ensure_ascii=False), content_type='application/json')
        #修改用户
        elif status == 3:
            userName = req.POST['username']
            Pwd = req.POST['pwd']
            userPhone= req.POST['userphone']
            user = Top_Register_User.userManager.get(user=userName)
            user.userphone = userPhone
            user.pwd = Pwd
            user.save()
        #新增用户
        elif status==1:
            username = req.POST['username']
            pwd = req.POST['pwd']
            phone = req.POST.get('userphone', default=None)
            if username == '':
                data = {"code": 200, "msg": '用户名不能为空'}
                return HttpResponse(json.dumps(data, ensure_ascii=False))
            elif not Top_Register_User.userManager.get(user__exact=username):
                new_user = Top_Register_User.userManager.create(username, pwd, phone)
                new_user.save()
                data = {"code": 200, "msg": '添加成功'}
                return HttpResponse(json.dumps(data,ensure_ascii=False))
            else:
                data={"code": 200, "msg": '请从新输入'}
                return HttpResponse(json.dumps(data,ensure_ascii=False))
        else:
                data={'code':200,'msg': '请确认请求状态'}
                return HttpResponse(json.dumps(data, ensure_ascii=False))
    else:
        data = {'code': 200, 'msg': '请求格式有误，请重试！'}
        HttpResponse(json.dumps(data, ensure_ascii=False))



def my_home(req):
    return render(req,'vipapp01/ld_home.html')
def my_home2(req):
    return render(req,'vipapp01/ld_home2.html')
def my_home3(req):
    return render(req,'vipapp01/ld_home3.html')


def celery(req):
    #sayhello.delay()
    sayhello()
    return HttpResponse('ok')

#缺少参数异常类
class info_lack(Exception):
    def __init__(self,Info):
        self.error=Info


#处理接口并且保存到数据库
def Interface_Case(req):
    if req.method=='POST':
        try:
            it_name=req.POST.get('it_name',default=None)
            data_type=req.POST.get('data_type',default=None)
            create_user=req.POST.get('create_user',default=None)
            headers=req.POST.get('headers',default=None)
            server=req.POST.get('server',default=None)
            port = req.POST.get('port',default=None)
            path = req.POST.get('path',default=None)
            parameter =req.POST.get('parameter',default=None)
            method = req.POST.get('method',default=None)
            protocol = req.POST.get('protocol',default=None)
            assertion = req.POST.get('assertion',default=None)       #json格式
            parameter_list=[it_name,data_type,create_user,headers,server,port,path,parameter,method,protocol,assertion]
            for i in parameter_list:
                if i == None:
                    raise info_lack('缺少参数,请重试')
        except info_lack as infolack:
            data={"code": 200,"msg":infolack}
            return HttpResponse(json.dumps(data))
        else:
            icase=Interface_Case.icaseManager.create(it_name,data_type,create_user,headers,server,port,path,parameter,method,protocol,assertion)
            icase.save()
            icaseitem=Interface_Case.icaseManager.filter(it_name=it_name).values()
            data = {"code": 200,"msg": '返回成功','data':icaseitem}
            return HttpResponse(json.dumps(data,ensure_ascii=False))

def action_icase(req):
    import requests
    if req.method=='POST':
        id=req.POST.get('id')
        case_obj=Interface_Case.icaseManager.filter(id=id).values()
        if case_obj['data_type']==1:    #表单
            data=case_obj['parameter']
            headers=case_obj['headers']
            it_reslut=requests.post(url=case_obj['method']+case_obj['server']+case_obj['port']+case_obj['path'],data=data,headers=headers)
            it_reslut=it_reslut.json()
            data={"code": 200,"msg": '返回成功','data':it_reslut}
            return HttpResponse(json.dumps(data,ensure_ascii=False))
        elif case_obj['data_type']==2:  #json
            parameter=case_obj['parameter']
            headers=case_obj['headers']
            it_reslut=requests.get(url=case_obj['method']+case_obj['server']+case_obj['port']+case_obj['path'],params=parameter,headers=headers)
            it_reslut=it_reslut.json()
            data={"code": 200,"msg": '返回成功','data':it_reslut}
            return HttpResponse(json.dumps(data,ensure_ascii=False))
        elif case_obj["data_type"]==3:  #xml
            pass
        else:
            data = {"code":200,"msg":"参数格式不正确"}
            return HttpResponse(json.dumps(data,ensure_ascii=False))


#test
def setcookie(req):
    H1=HttpResponse("ok")
    H1.set_signed_cookie("456","zzz12",salt="mima")
    H1.delete_cookie("1234")
    return HttpResponse().write("3232323")

def getcookie(req):
    COO=req.COOKIES['456']
    try:
        foo=req.get_signed_cookie('456',salt="mima")
    except:
        return HttpResponse("nook")
    print(foo)
    print(COO)
    prs=HttpResponse(COO)
    prs.write(foo)
    return prs














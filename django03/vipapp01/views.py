from django.shortcuts import render,redirect
from .models import *
from django.http import *
from django.urls import reverse
from django.db.models import F,Q
from datetime import timedelta,datetime
import json
from PIL import Image, ImageDraw, ImageFont


#注册
def register(req):
    return render(req,'vipapp01/register.html')

#注册处理
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
            data={"code": 200,"msg": '注册成功,请立即登陆',"data":reverse('vipapp01:login')}
            return HttpResponse(json.dumps(data))
                #redirect(reverse('vipapp01:login'))
        else:
            data={"code": 200,"msg": '账号已被注册，请重新注册',"data":reverse('vipapp01:register')}
            return HttpResponse(json.dumps(data))
                #redirect(reverse('vipapp01:register'))

#登陆
def login(req):
    return render(req,'vipapp01/login.html')

#登陆处理
def login_handle(req):
    if req.method=='POST':
        username=req.POST['username']
        pwd=req.POST['pwd']
        if Top_Register_User.userManager.filter(user=username):
            user=Top_Register_User.userManager.filter(user=username)
            for user in user:
                if user.pwd==pwd:
                    req.session['myuser']=username
                    req.session['pwd']=pwd
                    req.session.set_expiry(0)
                    data = {"code": 200, "msg": '返回成功', "data": reverse('vipapp01:login_show')}
                    return HttpResponse(json.dumps(data))
                        #redirect(reverse('vipapp01:login_show'))
                else:
                    data = {"code": 200, "msg": '返回成功', "data": reverse('vipapp01:login')}
                    return HttpResponse(json.dumps(data))
                        #redirect(reverse('vipapp01:login'))
        else:
            data = {"code": 200, "msg": '返回成功', "data": reverse('vipapp01:login')}
            return HttpResponse(json.loads(data))
                #redirect(reverse('vipapp01:register'))


def login_show(req):
    myuser=req.session['myuser']
    pwd=req.session['pwd']
    content={'myuser':myuser,'pwd':pwd}
    #req.session.clear()
    return render(req,'vipapp01/login_show.html',content)


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


def exception(req):
    #a=int('abc')
    #return HttpResponse('安全')
    return render(req,'vipapp01/register.html')





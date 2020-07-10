from django.http import HttpResponse,request
from django.shortcuts import render,redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin
#自定义中间件
class myexception(MiddlewareMixin):
    '''def process_exception(req,reps,exception):
        print('abc')
        return HttpResponse('df46')
    def process_response(req,resp,error1):
        return HttpResponse(error1)'''

class myexception1(MiddlewareMixin):
    '''def process_exception(req,reps,exception):
        print(123)
        #return None
        #return render(req,'vipapp01/login.html',status_code=600)
        return redirect(reverse('vipapp01:register'))'''
    '''def process_exception(req,reps,exception):
        print(123)
        return HttpResponse('df454')
    def process_response(req,resp,error1):
        #return render(req,'vipapp01/register.html')
        #return redirect(reverse('vipapp01:login'))
        return HttpResponse(2333)'''
    '''def process_template_response(self,req,resp):
        print('zld')
        return render(req,'vipapp01/login.html')'''
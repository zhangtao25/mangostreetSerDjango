# Create your views here.
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
import time, random, os, json
from django.forms.models import model_to_dict
from .models import *
from time import sleep
import threading


# 获取验证码
@require_http_methods(['GET'])
def vcode(request):
    print(request.GET)
    user_account = request.GET.get('user_account')
    check_results = check_user_account_is_exists(user_account)
    if len(check_results) == 0:
        user = User()
        vcode = str(random.randrange(100000, 999999))
        user.user_account = user_account
        user.user_password = ""
        user.user_nickname = ""
        user.user_img = "default.png"
        user.user_isdelete = 0
        user.user_isactive = 0
        user.token = user_account
        user.vcode = vcode
        user.save()
        t = threading.Thread(target=delete_expired_users, args=[user_account])
        t.start()
        res = {
            'result': True,
            'errorCode': None,
            'errorMessage': None,
            'response': {
                'vcode': vcode
            }
        }
        return HttpResponse(json.dumps(res), content_type='application/json')
    else:
        res = {
            'result': False,
            'errorCode': 1000,
            'errorMessage': '该邮箱已注册',
            'response': {}
        }
        return HttpResponse(json.dumps(res), content_type='application/json')


def check_user_account_is_exists(user_account):
    return User.objects.filter(user_account=user_account)


# 注册
@require_http_methods(['POST'])
def reg(request):
    user_account = request.POST.get('user_account')
    user_password = ''
    vcode = request.POST.get('vcode')
    print(user_account,vcode)
    # 检验有没有匹配的
    user = User.objects.filter(user_account=user_account, vcode=vcode)
    length = len(user)
    if length == 0:
        res = {
            'result': False,
            'errorCode': 2222,
            'errorMessage': '验证码错误',
            'response': {}
        }
        return HttpResponse(json.dumps(res), content_type='application/json')
    else:
        _user = User.objects.get(user_account=user_account)
        _user.user_isactive = True
        _user.user_password = user_password
        _user.save()
        res = {
            'result': True,
            'errorCode': None,
            'errorMessage': None,
            'response': '激活成功'
        }
        return HttpResponse(json.dumps(res), content_type='application/json')


@require_http_methods(['POST'])
def login(request):
    user_account = request.POST.get('user_account')
    user_password = request.POST.get('user_password')
    # 检验有没有匹配的
    print(user_account,user_password)
    user = User.objects.filter(user_account=user_account, user_password=user_password)
    length = len(user)
    if length == 0:
        res = {
            'result': False,
            'errorCode': 5545,
            'errorMessage': '账号密码错误',
            'response': {}
        }
        return HttpResponse(json.dumps(res), content_type='application/json')
    else:
        _user = User.objects.filter(user_account=user_account, user_password=user_password)
        _t = model_to_dict(_user[0])
        res = {
            'result': True,
            'errorCode': None,
            'errorMessage': None,
            'response': {
                'token':_t['token']
            }
        }
        return HttpResponse(json.dumps(res), content_type='application/json')

def delete_expired_users(user_account):
    # 设置十分钟有效
    sleep(60 * 10)
    User.objects.filter(user_account=user_account, user_isactive=0).delete()

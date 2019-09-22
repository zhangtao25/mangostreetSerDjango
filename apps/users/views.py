# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
import time, random, os, json
from django.forms.models import model_to_dict
from .models import *
from time import sleep
import threading

# 装饰器校验token，刚学的ovo
def check_token_decorator(decorator_arg):
    def _check_token(func):
        def __check_token(request, *args, **kwargs):
            print(request, args, kwargs,decorator_arg)
            token = request.META.get("HTTP_AUTHORIZATION")
            check_token_res = check_token(token)
            if len(check_token_res) == 0:
                res = {
                    'result': False,
                    'errorCode': 8888,
                    'errorMessage': 'token校验错误',
                    'response': {}
                }
                response = HttpResponse()
                response.content = json.dumps(res)
                response.status_code = 403
                return response
            return func(request, *args, **kwargs)
        return __check_token
    return _check_token


# 获取验证码
@require_http_methods(['GET'])
def vcode(request):
    print(request.GET)
    user_account = request.GET.get('user_account')
    check_results = check_user_account_is_exists(user_account)
    if len(check_results) == 0:
        user = User()
        vcode = str(random.randrange(100000, 999999))
        user.user_id = inspection_repeatability()
        user.user_account = user_account
        user.user_password = ""
        user.user_nickname = ""
        user.user_img = "default.jpeg"
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
    user_password =request.POST.get('user_password')
    user_nickname =request.POST.get('user_nickname')
    vcode = request.POST.get('vcode')
    print(user_account,vcode)
    # 检验有没有匹配的
    user = User.objects.filter(user_account=user_account, vcode=vcode)
    if not user.exists():
        res = {
            'result': False,
            'errorCode': 2222,
            'errorMessage': '验证码错误',
            'response': {}
        }
        # return HttpResponse(json.dumps(res), content_type='application/json')
        return JsonResponse(data=res)
    else:
        _user = User.objects.get(user_account=user_account)
        _user.user_isactive = True
        _user.user_password = user_password
        _user.user_nickname = user_nickname
        _user.save()
        print("注册成功")
        os.mkdir('./static/users/' + _user.user_account)
        with open('./static/img/default.jpg','rb') as fr:
            context=fr.read()
        topath = './static/users/'+_user.user_account+'/'+'default.jpg'
        with open(topath,'wb') as fr:
            fr.write(context)
        res = {
            'result': True,
            'errorCode': None,
            'errorMessage': None,
            'response': '账号注册成功'
        }
        # return HttpResponse(json.dumps(res), content_type='application/json')
        return JsonResponse(data=res)


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

# 以上不需要鉴权


def info(request):
    token = request.META.get("HTTP_AUTHORIZATION")
    check_token_res = check_token(token)
    if len(check_token_res) == 0:
        res = {
            'result': False,
            'errorCode': 8888,
            'errorMessage': 'token校验错误',
            'response': {}
        }
        response = HttpResponse()
        response.content = json.dumps(res)
        response.status_code = 403
        return response

    res = {
        'result': True,
        'errorCode': None,
        'errorMessage': None,
        'response': model_to_dict(check_token_res[0])
    }
    return HttpResponse(json.dumps(res), content_type='application/json')


@check_token_decorator('test')
def updateinfo(request):
    token = request.META.get("HTTP_AUTHORIZATION")


    # 注意判断，萌新入坑，还不了解高端写法ovo
    if request.POST.get('user_nickname'):
        user_nickname = request.POST.get('user_nickname')
        User.objects.filter(token=token).update(user_nickname=user_nickname)
    elif request.POST.get('user_sex'):
        user_sex = request.POST.get('user_sex')
        User.objects.filter(token=token).update(user_sex=user_sex)
    elif request.POST.get('user_birthday'):
        user_birthday = request.POST.get('user_birthday')
        User.objects.filter(token=token).update(user_birthday=user_birthday)
    elif request.FILES.getlist('user_img'):
        user_img = request.FILES.getlist('user_img')
        _user_img = 'default' + str(random.randrange(100000000, 999999999)) + '.jpg'
        User.objects.filter(token=token).update(user_img=_user_img)
        _user = User.objects.get(token=token)
        dirPath = './static/users/'+_user.user_account+'/'
        if (os.path.exists(dirPath + _user_img)):
            # os.remove(dirPath + "default.jpg")
            print ('移除后test 目录下有文件：%s' % os.listdir(dirPath))
        else:
            print("要删除的文件不存在！")
        imgfilepath = dirPath + _user_img
        with open(imgfilepath, 'wb') as imgfile:
            for info in user_img[0].chunks():
                imgfile.write(info)



    res = {
        'result': True,
        'errorCode': None,
        'errorMessage': None,
        'response': {}
    }
    return HttpResponse(json.dumps(res), content_type='application/json')

def delete_expired_users(user_account):
    # 设置十分钟有效
    sleep(60 * 10)
    User.objects.filter(user_account=user_account, user_isactive=0).delete()

def inspection_repeatability():
    user_id = str(random.randrange(100000000, 999999999))
    _user = User.objects.filter(user_id = user_id)
    if len(_user) !=0:
        inspection_repeatability()
    return user_id

def check_token(token):
    user = User.objects.filter(token=token)
    return user
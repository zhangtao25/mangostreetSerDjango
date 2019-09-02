# Create your views here.
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
import time,random,os,json
from .models import *
from django.core.mail import send_mail
from django.conf import settings


# 获取验证码
@require_http_methods(['GET'])
def vcode(request):
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
        user.token = 'wfeafwasfasfasfasfas'
        user.vcode = vcode
        user.save()
        return HttpResponse(vcode)
    else:
        return HttpResponse('no',content_type='application/json')

#注册
@require_http_methods(['POST'])
def reg(request):
    user_account = request.POST.get('user_account')
    user_nickname = request.POST.get('user_nickname')
    user_password = request.POST.get('user_password')
    user_img = request.POST.get('user_img')
    v_code =''
    str = '1234567890qwertyuiopasdfghjklzxcvbnm'
    for i in range(0, 4):
        v_code += str[random.randrange(0, len(str))]
    token = time.time() + random.randrange(1, 100000)
    user_token = str(token)
    f = request.FILES["userImg"]
    userImg = os.path.join(settings.MDEIA_ROOT, user_account + ".png")
    with open(userImg, "wb") as fp:
        for data in f.chunks():
            fp.write(data)
    try:
        user = User.objects.get(user_account=user_account)
    except User.DoesNotExist:
        #用户名不存在
        user=None
    if user:
        return HttpResponse("用户已存在")
    user = User.createuser(user_account, user_password,user_nickname, user_img, user_token,v_code)
    user.save()

    request.session["username"] = user_account
    request.session["token"] = user_token
    subject ='芒果街欢迎你'
    message = ''
    sender = settings.EMAIL_FROM
    receiver = user_account
    html_message1 = '<h1>%s,欢迎你成为芒果街注册会员</h1>下面是您的验证码<br/><h2>验证码：%s</h2>'%(user_nickname,user.v_code)
    send_mail(subject,message,sender,receiver,html_message=html_message1)
    #校验验证码
    try:
        user=User.objects.get(v_code=v_code)
        if user.v_code != request.POST.get("v_code"):
            return HttpResponse("验证码输入错误，请重新输入")
        else:
            return HttpResponse("恭喜你注册成功")
    except User.DoesNotExist as e:
        return HttpResponse("尚未注册，请注册")


def check_user_account_is_exists(user_account):
    return User.objects.filter(user_account=user_account)
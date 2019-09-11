# Create your views here.
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.forms.models import model_to_dict
import json
from .models import Notes
import os,threading
import random
import tinify
from apps.users.models import User

# 查询token
def check_token(token):
    user = User.objects.filter(token=token)
    return user

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


# 可以接收到列表中的规定的请求
@require_http_methods(['POST'])
@check_token_decorator('test')
def index(request):
    return add_note(request)

@require_http_methods(['GET'])
@check_token_decorator('test')
def get_by_id(request,id):
    queryset = Notes.objects.filter(id=id)
    data = []
    for i in queryset:
        data.append(model_to_dict(i))
    return HttpResponse(json.dumps(data), content_type='application/json')


@require_http_methods(['GET'])
@check_token_decorator('test')
def get_all(request):
    queryset = Notes.objects.filter()
    data = []
    for i in queryset:
        data.append(model_to_dict(i))
    return HttpResponse(json.dumps(data), content_type='application/json')


tinify.key = "38Dw8ftlF8N1Scl8ZWbBQ7bXSYHy7GcQ"
    # 这里就是通过tingPng压缩图片的核心代码
def compress_core(file, outputFile):
    source = tinify.from_file(file)  # 压缩指定文件
    source.to_file(outputFile)


@require_http_methods(['POST'])
@check_token_decorator('test')
def add_note(request):
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
    img_files = request.FILES.getlist('myfiles')
    list1 = []
    str = '1234567890qwertyuiopasdfghjklzxcvbnm'
    id_str = ''
    for i in range(0, 24):
        id_str += str[random.randrange(0, len(str))]
    os.mkdir('./static/notes/' + id_str)
    os.mkdir('./static/notes/' + id_str + '/cover')
    os.mkdir('./static/notes/' + id_str + '/images')
    for img in img_files:
        list1.append(img.name)
        imgfilepath = os.path.join('./static/notes'+'/'+id_str+'/images',img.name)
        with open(imgfilepath,'wb') as imgfile:
            for info in img.chunks():
                imgfile.write(info)
                t1 = threading.Thread(target=compress_core,args=(imgfilepath,imgfilepath))
                t1.start()

    imgfilepath = os.path.join('./static/notes'+'/'+id_str+'/cover',img_files[-1].name)
    with open(imgfilepath,'wb') as imgfile:
        for info in img_files[-1].chunks():
            imgfile.write(info)
            t2 = threading.Thread(target=compress_core, args=(imgfilepath, imgfilepath))
            t2.start()
    images=""
    j=1
    for i in list1:
        images += i
        j += 1
        if j <=len(list1):
            images += ","
    note1=Notes()
    note1.images=images
    note1.cover=list1[-1]
    note1.title = request.POST.get('title')
    note1.desc = request.POST.get('desc')
    note1.id=id_str
    note1.user_id=model_to_dict(check_token_res[0])['user_id']
    note1.save()
    return HttpResponse('OK')





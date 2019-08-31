# Create your views here.
from django.http import HttpResponse,JsonResponse
from django.views.decorators.http import require_GET,require_POST,require_http_methods
from django.forms.models import model_to_dict
from django.core import serializers
import json
import time
from .models import Notes
from django.conf import settings
import os
import random
# 可以接收到列表中的规定的请求
@require_http_methods(['GET', 'POST'])
def index(request):
    if request.method == 'POST':
        return add_note(request)
    elif request.method == 'GET':
        return get_all_notes(request)

def get_note_by_id(request):
    id = request.GET['id']
    queryset = Notes.objects.filter(id=id)
    data = []
    for i in queryset:
        data.append(model_to_dict(i))
    return HttpResponse(json.dumps(data), content_type='application/json')


# methods:GET
def get_all_notes(request):
    queryset = Notes.objects.filter()
    data = []
    for i in queryset:
        data.append(model_to_dict(i))
    return HttpResponse(json.dumps(data), content_type='application/json')


# methods:POST
def add_note(request):
    # for代军：
    #     字段的话就是note models里的字段，每个我都会传，而且还有不定数量的图片文件，有两类，一类
    #     是cover，这个是外部浏览笔记的时候的封面，一类是images，这个是笔记详情页的不定数量的图片。
    #     这块你来操作，周六起来搞！
    #     ps：你可以用postman自测

    img_files = request.FILES.getlist('myfiles')
    list1 = []
    str = '1234567890qwertyuiopasdfghjklzxcvbnm'
    userid_str = ''
    id_str = ''
    for i in range(0, 24):
        userid_str += str[random.randrange(0, len(str))]
    for i in range(0, 24):
        id_str += str[random.randrange(0, len(str))]
    os.mkdir('./static/notes/' + id_str)
    for img in img_files:
        list1.append(img.name)
        imgfilepath = os.path.join('./static/notes'+'/'+id_str+'/',img.name)
        with open(imgfilepath,'wb') as imgfile:
            for info in img.chunks():
                imgfile.write(info)
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
    note1.user_id=userid_str
    note1.save()
    return HttpResponse('OK')


# ↓↓↓以下是例子
# 只能接收get的请求,如果是post请求访问则直接报错,无法接收
@require_GET
def rgt(request):
    return HttpResponse('GET请求')


# 只能接收post的请求,如果是get请求访问则直接报错,无法接收
@require_POST
def rpt(request):
    return HttpResponse('POST请求')


# 可以接收到列表中的规定的请求
@require_http_methods(['GET', 'POST'])
def gpt(request):
    return HttpResponse('收到')

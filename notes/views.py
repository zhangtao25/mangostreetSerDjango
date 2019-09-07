# Create your views here.
from django.http import HttpResponse
from django.views.decorators.http import require_GET,require_POST,require_http_methods
from django.forms.models import model_to_dict
import json
from .models import Notes
import os,threading
import random
import tinify


# 可以接收到列表中的规定的请求
@require_http_methods(['POST'])
def index(request):
    return add_note(request)


def get_by_id(request,id):
    queryset = Notes.objects.filter(id=id)
    data = []
    for i in queryset:
        data.append(model_to_dict(i))
    return HttpResponse(json.dumps(data), content_type='application/json')


def get_all(request):
    print(request.META.get("HTTP_AUTHORIZATION"))
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



    # list1.append(img_files[0].name)
    imgfilepath = os.path.join('./static/notes'+'/'+id_str+'/cover',img_files[-1].name)
    with open(imgfilepath,'wb') as imgfile:
        for info in img_files[-1].chunks():
            imgfile.write(info)
            # image = Image.open(imgfilepath)
            # w, h =image.size
            # dImg=image.resize((int(w/5),int(h/5)),Image.ANTIALIAS)
            # dImg.save(imgfilepath)
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
    note1.user_id=userid_str
    note1.save()
    return HttpResponse('OK')

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.http import require_GET,require_POST,require_http_methods
from django.forms.models import model_to_dict
import json
from .models import Notes

# 可以接收到列表中的规定的请求
@require_http_methods(['GET', 'POST'])
def index(request):
    if request.method == 'POST':
        return add_note(request)
    elif request.method == 'GET':
        return get_all_notes(request)

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
    return HttpResponse('这里编写添加note接口')

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
from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

# Create your views here.


def test(request) :
    SECRET = '53b9eef72ed85fda0f72954c79f3c9e5'
    APPID = request.GET.get('APPID')
    CODE = request.GET.get('CODE')
    response = requests.get('https://api.weixin.qq.com/sns/oauth2/access_token?appid='+APPID+'&secret='+SECRET+'&code='+CODE+'&grant_type=authorization_code')
    # 返回响应头
    # print (response.status_code)
    return HttpResponse(response)
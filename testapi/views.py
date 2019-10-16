from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
import time

# Create your views here.


def test(request) :
    time.sleep(5)
    response = 'sssss'
    return HttpResponse(response)
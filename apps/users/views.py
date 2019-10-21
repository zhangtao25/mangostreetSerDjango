from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from users.models import User
from users.serializers import UserSerializer
from users.models import Follow
from users.serializers import FollowSerializer
from django.http import JsonResponse
import time


class AuthticationView(BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get("HTTP_AUTHORIZATION")
        token_obj = User.objects.filter(token=token).first()
        if not token_obj:
            raise exceptions.AuthenticationFailed('用户认证失败')
        return (token_obj.user_account, token_obj)

    def authenticate_header(self, request):
        pass


class AuthView(APIView):
    def post(self, request, *args, **kwargs):
        ret = {'code': 1000, 'msg': None}
        user_account = request._request.POST.get('user_account')
        user_password = request._request.POST.get('user_password')
        print(user_password, user_account)
        obj = User.objects.filter(user_account=user_account, user_password=user_password).first()
        if not obj:
            ret['code'] = '1001'
            ret['msg'] = '用户名密码错误'
        token = str(time.time()) + user_account
        User.objects.update_or_create(user_account=obj, defaults={'token': token})
        ret['response'] = {'token': token}
        ret['result'] = True
        return JsonResponse(ret)


class UserViewSet(viewsets.ModelViewSet):
    """
    这个视图集自动提供“列表”和“详细”操作。
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class FollowViewSet(viewsets.ModelViewSet):
    # authentication_classes = [AuthticationView]
    """
    这个视图集自动提供“列表”和“详细”操作。
    """
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer

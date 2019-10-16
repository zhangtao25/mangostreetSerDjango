from rest_framework import viewsets
from users.models import User
from users.serializers import UserSerializer
from users.models import Follow
from users.serializers import FollowSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    这个视图集自动提供“列表”和“详细”操作。
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class FollowViewSet(viewsets.ModelViewSet):
    """
    这个视图集自动提供“列表”和“详细”操作。
    """
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer

from rest_framework import viewsets
from users.models import User
from users.serializers import UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    这个视图集自动提供“列表”和“详细”操作。
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

from django.contrib import admin
from django.urls import include, path

from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import serializers, viewsets, routers
# from snippets.views import BookInfoViewSet

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
# router.register(r'books', views.)  # 向路由器中注册视图集


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('notes/', include('apps.notes.urls')),
    path('users/', include('apps.users.urls')),
    path('admin/', admin.site.urls),
    path('snippets/', include('snippets.urls')),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from notes.models import Note
from notes.serializers import NoteSerializer
from rest_framework import permissions
from rest_framework import renderers

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    自定义权限，只允许对象的所有者编辑它。
    """

    def has_object_permission(self, request, view, obj):
        # 任何请求都允许有读权限，
        # 所以我们总是允许GET, HEAD或OPTIONS请求。
        if request.method in permissions.SAFE_METHODS:
            return True

        # 写权限只允许给代码段的所有者。
        return obj.owner == request.user


class NoteViewSet(viewsets.ModelViewSet):
    """
    这个viewset会自动提供' list '， ' create '， ' retrieve '，

    “更新”和“销毁”动作。

    此外，我们还提供一个额外的“highlight”行动。
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
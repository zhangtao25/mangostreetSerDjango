from rest_framework import viewsets
from notes.models import Note
from notes.models import Like
from notes.models import Collect
from notes.serializers import NoteSerializer
from notes.serializers import LikeSerializer
from notes.serializers import CollectSerializer
from users.views import AuthticationView


class NoteViewSet(viewsets.ModelViewSet):
    # authentication_classes = [AuthticationView]
    """
    这个视图集自动提供“列表”和“详细”操作。
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class LikeViewSet(viewsets.ModelViewSet):
    """
    这个视图集自动提供“列表”和“详细”操作。
    """
    # queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def get_queryset(self):
        return Like.objects.all()

    def perform_create(self, serializer):
        # 先保存“赞”
        like = serializer.save()
        like.save()
        # 通过点赞的note_id获取这篇笔记的点赞数量
        like_list = Like.objects.filter(note_id=like.note_id)
        # 把这篇笔记取出来
        note = Note.objects.get(note_id=like.note_id)
        # 把点完赞的数量赋值给note对象
        note.likes = len(like_list)
        note.save()


class CollectViewSet(viewsets.ModelViewSet):
    """
    这个视图集自动提供“列表”和“详细”操作。
    """
    queryset = Collect.objects.all()
    serializer_class = CollectSerializer
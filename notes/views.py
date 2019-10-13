from rest_framework import viewsets
from notes.models import Note
from notes.models import Like
from notes.models import Collect
from notes.serializers import NoteSerializer
from notes.serializers import LikeSerializer
from notes.serializers import CollectSerializer


class NoteViewSet(viewsets.ModelViewSet):
    """
    这个视图集自动提供“列表”和“详细”操作。
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class LikeViewSet(viewsets.ModelViewSet):
    """
    这个视图集自动提供“列表”和“详细”操作。
    """
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


class CollectViewSet(viewsets.ModelViewSet):
    """
    这个视图集自动提供“列表”和“详细”操作。
    """
    queryset = Collect.objects.all()
    serializer_class = CollectSerializer
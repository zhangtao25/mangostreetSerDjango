from rest_framework import viewsets
from notes.models import Note
from notes.serializers import NoteSerializer


class NoteViewSet(viewsets.ModelViewSet):
    """
    这个视图集自动提供“列表”和“详细”操作。
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
from rest_framework import viewsets
from notes.models import Note
from notes.models import Like
from notes.models import Collect
from notes.models import Image
from notes.serializers import NoteSerializer
from notes.serializers import LikeSerializer
from notes.serializers import CollectSerializer
from notes.serializers import ImageSerializer
from users.views import AuthticationView


class NoteViewSet(viewsets.ModelViewSet):
    # authentication_classes = [AuthticationView]
    """
    这个视图集自动提供“列表”和“详细”操作。
    """
    # queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def get_queryset(self):
        Notes = Note.objects.all()
        for note in Notes:
            note.images = ''
            Images = Image.objects.filter(note_id=note.note_id)
            arr = []
            for image in Images:
                arr.append(image.image.path)
            note.images = list(arr)
            note.save()
        return Note.objects.all()


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

class ImageViewSet(viewsets.ModelViewSet):
    """
    这个视图集自动提供“列表”和“详细”操作。
    """
    serializer_class = ImageSerializer

    def get_queryset(self):
        return Image.objects.all()

    def perform_create(self, serializer):
        image = serializer.save()
        image.save()
        # 把这篇笔记取出来
        image_list = Image.objects.filter(note_id=image.note_id)
        note = Note.objects.get(note_id=image.note_id)
        arr = []
        for image in image_list:
            arr.append(image.image.path)
        note.images = list(arr)
        note.save()
from rest_framework import serializers
from notes.models import Note
from notes.models import Like
from notes.models import Collect

class NoteSerializer(serializers.ModelSerializer):
    user_nickname = serializers.CharField(source='user.user_nickname')
    user_id = serializers.CharField(source='user.user_id')
    class Meta:
        model = Note
        # fields = [
        #     'id', 'title', 'type',
        #     'desc', 'likes', 'cover',
        #     'collects','images','user_nickname','user_id']
        fields = "__all__"

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"

class CollectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collect
        fields = "__all__"
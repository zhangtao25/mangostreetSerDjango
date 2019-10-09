from rest_framework import serializers
from notes.models import Note


class NoteSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=255)
    type = serializers.ChoiceField(choices=[('normal','normal'),('video','video')], default='normal')
    desc = serializers.CharField(required=False, allow_blank=True, max_length=255)
    likes = serializers.BooleanField(default=0)
    cover = serializers.ImageField()
    collects = serializers.IntegerField(default=0)
    images = serializers.ImageField()

    def create(self, validated_data):
        """
        根据已验证的数据，创建并返回一个新的“Note”实例。
        """
        return Note.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        给定已验证的数据，更新并返回现有的“Note”实例。
        """
        instance.id = validated_data.get('id', instance.id)
        instance.title = validated_data.get('title', instance.title)
        instance.type = validated_data.get('type', instance.type)
        instance.desc = validated_data.get('desc', instance.desc)
        instance.likes = validated_data.get('likes', instance.likes)
        instance.cover = validated_data.get('cover', instance.cover)
        instance.collects = validated_data.get('collects', instance.collects)
        instance.images = validated_data.get('images', instance.images)
        instance.save()
        return instance
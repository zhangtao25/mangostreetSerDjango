from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.Serializer):

    user_account = serializers.CharField(read_only=True)
    user_id = serializers.CharField(required=False, allow_blank=True, max_length=255)
    user_sex = serializers.CharField(required=False, allow_blank=True, max_length=255)
    user_password = serializers.CharField(required=False, allow_blank=True, max_length=255)
    user_nickname = serializers.CharField(max_length=20)
    user_img = serializers.ImageField()
    user_isdelete = serializers.BooleanField(default=False)
    user_isactive = serializers.BooleanField(default=False)
    token = serializers.CharField(required=False, allow_blank=True, max_length=255)
    vcode = serializers.CharField(required=False, allow_blank=True, max_length=255)

    def create(self, validated_data):
        """
        根据已验证的数据，创建并返回一个新的“User”实例。
        """
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        给定已验证的数据，更新并返回现有的“User”实例。
        """
        instance.user_account = validated_data.get('user_account', instance.user_account)
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.user_sex = validated_data.get('user_sex', instance.user_sex)
        instance.user_password = validated_data.get('user_password', instance.user_password)
        instance.user_nickname = validated_data.get('user_nickname', instance.user_nickname)
        instance.user_img = validated_data.get('user_img', instance.user_img)
        instance.user_isdelete = validated_data.get('user_isdelete', instance.user_isdelete)
        instance.user_isactive = validated_data.get('user_isactive', instance.user_isactive)
        instance.token = validated_data.get('token', instance.token)
        instance.vcode = validated_data.get('vcode', instance.vcode)
        instance.save()
        return instance
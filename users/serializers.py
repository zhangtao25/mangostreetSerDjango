from rest_framework import serializers
from users.models import User
from users.models import Follow

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = [
        #     'user_account', 'user_id', 'user_sex',
        #     'user_password', 'user_nickname', 'user_img',
        #     'user_isdelete','user_isactive','token',
        #     'vcode']
        fields = "__all__"

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = "__all__"
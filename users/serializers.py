from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'user_account', 'user_id', 'user_sex',
            'user_password', 'user_nickname', 'user_img',
            'user_isdelete','user_isactive','token',
            'vcode']
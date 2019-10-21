from django.contrib import admin
from users.models import User
from users.models import Follow


class UserAdmin(admin.ModelAdmin):
    list_display = (
    'user_account', 'user_id', 'user_sex', 'user_password', 'user_nickname', 'user_img', 'user_isdelete',
    'user_isactive', 'token')


class FollowAdmin(admin.ModelAdmin):
    list_display = ('created', 'follow_id', 'be_follower', 'follower')


admin.site.register(User, UserAdmin)
admin.site.register(Follow, FollowAdmin)

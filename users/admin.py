from django.contrib import admin
from users.models import User


class UserAdmin(admin.ModelAdmin):
    list_display=('user_account','user_id','user_sex','user_password','user_nickname','user_img','user_isdelete','user_isactive','token')


admin.site.register(User, UserAdmin)
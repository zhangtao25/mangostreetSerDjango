from django.db import models

# Create your models here.
class User(models.Model):
    # 用户账号，要唯一
    user_account=models.CharField(primary_key=True,max_length=50,unique=True)
    # 密码
    user_password=models.CharField(max_length=20)
    # 昵称
    user_nickname=models.CharField(max_length=20)
    # 头像名字
    user_img=models.CharField(max_length=150)
    user_isdelete=models.BooleanField(max_length=2,default=False)
    user_isactive=models.BooleanField(max_length=2,default=True)
    # touken验证值，每次登陆之后都会更新
    token=models.CharField(max_length=50)
    vcode=models.CharField(max_length=10)
    class Meta():
        db_table = "users"
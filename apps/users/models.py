from django.db import models

# Create your models here.
class Users(models.Model):
    user_id = models.CharField(max_length=20)
    user_sex = models.IntegerField(default=1)
    user_account=models.CharField(primary_key=True,max_length=50,unique=True)
    user_password=models.CharField(max_length=20)
    user_nickname=models.CharField(max_length=20)
    user_img=models.CharField(max_length=150)
    user_isdelete=models.BooleanField(max_length=2,default=False)
    user_isactive=models.BooleanField(max_length=2,default=True)
    token=models.CharField(max_length=50)
    vcode=models.CharField(max_length=10)

class Follows(models.Model):
    follow_id = models.CharField(max_length=20,primary_key=True)
    user_id = models.CharField(max_length=20)
    follow_user_id = models.CharField(max_length=20)
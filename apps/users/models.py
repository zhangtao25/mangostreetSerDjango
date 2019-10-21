from django.db import models
import uuid


class User(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user_id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    user_account = models.CharField(max_length=50)
    user_sex = models.IntegerField(default=1)
    user_password = models.CharField(max_length=20)
    user_nickname = models.CharField(max_length=20,default='新用户')
    user_img = models.ImageField(upload_to='media/users/user_img', default='media/users/user_img/default.jpg')
    user_isdelete = models.BooleanField(default=False)
    user_isactive = models.BooleanField(default=False)
    token = models.CharField(max_length=50,default=False)
    vcode = models.CharField(max_length=50,default=False)

    class Meta:
        ordering = ['created']



class Follow(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    follow_id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    be_follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='be_follower')
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')

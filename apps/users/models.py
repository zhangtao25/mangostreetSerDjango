from django.db import models
# from notes import Note

class User(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user_id = models.CharField(primary_key=True, max_length=50, unique=True)
    user_account = models.CharField(max_length=50)
    user_sex = models.IntegerField(default=1)
    user_password = models.CharField(max_length=20)
    user_nickname = models.CharField(max_length=20)
    user_img = models.ImageField(upload_to='media/users/user_img')
    user_isdelete = models.BooleanField(default=False)
    user_isactive = models.BooleanField(default=False)
    token = models.CharField(max_length=50)
    vcode = models.CharField(max_length=50)

    class Meta:
        ordering = ['created']


class Follow(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    follow_id = models.CharField(primary_key=True, max_length=50, unique=True)
    be_follower = models.ForeignKey(User, on_delete=models.CASCADE,related_name='be_follower')
    follower = models.ForeignKey(User, on_delete=models.CASCADE,related_name='follower')

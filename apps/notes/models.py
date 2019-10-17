from django.db import models
from users.models import User


class Note(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    type = models.CharField(choices=[('normal','normal'),('video','video')], default='normal', max_length=10)
    desc = models.TextField()
    likes = models.IntegerField(default=0)
    cover = models.ImageField(upload_to='avatars/')
    collects = models.IntegerField(default=0)
    images = models.ImageField(max_length=500,upload_to='avatars/')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    class Meta:
        ordering = ['created']


class Collect(models.Model):
    collect_id = models.CharField(max_length=50, primary_key=True)
    # user_id = models.CharField(max_length=50)
    # note_id = models.CharField(max_length=50)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    note = models.ForeignKey(Note,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    like_id = models.CharField(max_length=50, primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    note = models.ForeignKey(Note,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


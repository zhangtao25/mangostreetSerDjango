from django.db import models
from users.models import User
import uuid


class Note(models.Model):
    note_id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    type = models.CharField(choices=[('normal','normal'),('video','video')], default='normal', max_length=10)
    desc = models.TextField()
    likes = models.IntegerField(default=0)
    # cover = models.ImageField(upload_to='avatars/')
    collects = models.IntegerField(default=0)
    images = models.ImageField(max_length=500,upload_to='media/notes/images/')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    class Meta:
        ordering = ['created']


class Collect(models.Model):
    collect_id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    note = models.ForeignKey(Note,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    like_id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    note = models.ForeignKey(Note,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


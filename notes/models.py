from django.db import models


class Note(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    type = models.CharField(choices=[('normal','normal'),('video','video')], default='normal', max_length=10)
    desc = models.TextField()
    likes = models.IntegerField(default=0)
    cover = models.ImageField(upload_to='avatars/')
    user_id = models.CharField(max_length=50)
    collects = models.IntegerField(default=0)
    images = models.ImageField(max_length=500,upload_to='avatars/')
    class Meta:
        ordering = ['created']

class Follow(models.Model):
    follow_id = models.CharField(max_length=50, primary_key=True)
    user_id = models.CharField(max_length=50)
    follow_user_id = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)